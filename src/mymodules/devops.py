#!/usr/bin/env python3
# usage: python3 [script].py [--work_home=] [--git_repo=] [--git_branches=] [--project_name=] [--profile=] [--to_ip=] [--to_project_home=] [--to_process_name=] [--to_java_opts=] [--git_merged_branch=] [--git_tag_version=] [--git_tag_comment=] [--git_delete_temp_branch=]
# eg: python3 devops.py --work_home=/tmp/devops --git_repo=git@192.168.1.248:mall/config-server.git --git_branches=develop --project_name=config-server --profile=dev --to_ip=192.168.1.248 --to_project_home=/home/project/mama_config_server --to_process_name=config-server --to_java_opts="-Xms768m -Xmx768m" --git_merged_branch= --git_tag_version= --git_tag_comment= --git_delete_temp_branch=0
# 约定1：远程执行脚本路径（工程见devops-sh）：/home/devops/restart_jar.sh
# 约定2：打包完毕上传至远程服务器[path_to_project_home]/web/目录下；远程服务器项目备份目录：[path_to_project_home]/backup/
# 其他：如果作为Python脚本脱离web容器独立运行的话，注意引入其他模块或配置文件的路径；
# 多分支发布时，临时分支命名格式：publish-temp-{%Y%m%d%H%M%S}

import os
import sys
import time
import subprocess
import getopt
import configparser

try:
    sys.path.append(os.path.realpath('.'))
    from src.mymodules.sshcmd import scp_cmd, ssh_cmd
except Exception as e:
    print('WARN:', 'import error, try another path..')
    from sshcmd import scp_cmd, ssh_cmd

# global variables
work_home = None
server_passport_config_location = 'src/configs/server_passport.properties'


def output_all(msg, resp=0, exit=False):
    print(msg if resp == 0 else f'{msg}, status_code: {resp}')
    if exit:
        sys.exit()
    else:
        sys.stdout.flush()


def output_strict(msg, resp):
    if resp != 0:
        output_error(msg, resp)
    else:
        output_std(msg)


def output_relaxed(msg, resp):
    if resp != 0:
        output_warn(msg, resp)
    else:
        output_std(msg)


def output_error(msg, resp=-1, exit=True):
    output_all(f'ERROR: {msg}', resp, exit)


def output_warn(msg, resp=-1):
    output_all(f'WARN: {msg}', resp)


def output_std(msg):
    output_all(f'INFO: {msg}')


def publish(git_repo, git_branches, project_name, profile, source_file_dir, to_ip, to_project_home, to_process_name,
            to_java_opts, git_merged_branch, git_tag_version, git_tag_comment, git_delete_temp_branch):
    # declare extra parameters
    is_standalone_branch = True
    git_branches_array = git_branches.split(',')

    # verify parameters
    if git_repo is None or git_repo.strip() == '' \
            or len(git_branches_array) == 0 \
            or project_name is None or project_name.strip() == '' \
            or profile is None or profile.strip() == '' \
            or to_ip is None or to_ip.strip() == '' \
            or to_project_home is None or to_project_home.strip() == '' \
            or to_process_name is None or to_process_name.strip() == '':
        output_error(
            f'required parameters cannot be empty: git_repo:{git_repo}, git_branches:{git_branches}, '
            f'project_name:{project_name}, profile:{profile}, to_ip:{to_ip}, to_project_home:{to_project_home}, to_process_name:{to_process_name}')

    if len(git_branches_array) > 1:
        is_standalone_branch = False
        filter(None, git_branches_array)
        if len(git_branches_array) == 0:
            output_error('parameter [git_branches] invalid')
        place_holder_branch = git_branches_array[0]
    else:
        place_holder_branch = git_branches_array[0]

    # read config.properties
    config = configparser.ConfigParser()
    config.read(server_passport_config_location)
    to_username = config.get(to_ip, 'username')
    to_password = config.get(to_ip, 'password')

    # local project home
    from_project_home = work_home + '/' + project_name

    output_std('>>> 清除历史项目痕迹，开始新的工作')
    resp = os.system(f'cd {work_home} && rm -rf {project_name}')
    output_strict('<<< 清除历史项目痕迹，开始新的工作', resp)

    output_std('>>> 克隆项目到发布系统本地')
    resp = os.system(f'cd {work_home} && git clone -b {place_holder_branch} {git_repo}')
    output_strict('<<< 克隆项目到发布系统本地', resp)

    generated_timestamped_branch = ''
    if not is_standalone_branch:
        # temporary branch generated strategy(when multiple branches)
        generated_timestamped_branch = "publish-temp-" + time.strftime("%Y%m%d%H%M%S", time.localtime())
        output_std(f'>>> 创建临时分支{generated_timestamped_branch}，并切到新分支上')
        resp = os.system(f'cd {from_project_home} && git checkout -b {generated_timestamped_branch}')
        output_strict(f'<<< 创建临时分支{generated_timestamped_branch}，并切到新分支上', resp)
        for each_branch in git_branches_array:
            output_std(f'>>> 在新分支上合并分支{each_branch}')
            resp = os.system(f'cd {from_project_home} && git merge {each_branch}')
            # ignore 256: merge: {branch} - not something we can merge  Did you mean this?
            output_strict(f'<<< 在新分支上合并分支{each_branch}', resp if resp != 256 else 0)

    output_std(f'>>> maven开始打包，打包环境：{profile}')
    resp = os.system(f'cd {from_project_home} && mvn clean package -Dmaven.test.skip=true -P {profile} -U')
    output_strict(f'<<< maven打包结束，打包环境：{profile}', resp)

    # lookup local file location
    output_std(f'>>> 检查本地jar包是否生成：{from_project_home}/{source_file_dir}')
    (status, filepath) = subprocess.getstatusoutput(f'ls {from_project_home}/{source_file_dir}/*.*ar')
    output_strict(f'<<< 检查本地jar包生成结果', status)

    # check if remote folders exist or create ones(the devopser should check the project home manually)
    output_std(f'>>> SSH远程检查文件夹是否存在...')
    ssh_cmd_result = ssh_cmd(to_ip, to_password,
                             [
                                 f'if [ ! -d {to_project_home}/web ]; then mkdir {to_project_home}/web; fi '
                                 f'&& if [ ! -d {to_project_home}/backup ]; then mkdir {to_project_home}/backup; fi'],
                             to_username)
    output_std(f'<<< SSH远程检查文件夹是否存在，状态：{ssh_cmd_result}')
    if ssh_cmd_result == 'FAILED':
        output_error('SSH远程检查文件夹是否存在失败！')

    output_std(f'>>> SCP远程上传文件开始...')
    scp_result = scp_cmd(to_ip, to_password, filepath, f'{to_project_home}/web/', to_username)
    output_std(f'<<< SCP远程上传文件结束，状态：{scp_result}')
    if scp_result == 'FAILED':
        output_error('SCP上传文件到远程服务器失败！')

    output_std(f'>>> SSH远程执行命令开始...')
    ssh_cmd_result = ssh_cmd(to_ip, to_password,
                             [f'sh /home/devops/restart_jar.sh {to_project_home} {to_process_name} "{to_java_opts}"'],
                             to_username)
    output_std(f'<<< SSH远程执行命令结束，状态：{ssh_cmd_result}')
    if ssh_cmd_result == 'FAILED':
        output_error('SSH远程执行命令失败！')

    if not is_standalone_branch:
        git_published_branch = generated_timestamped_branch
    else:
        git_published_branch = git_branches_array[0]
    resp = os.system(
        f'cd {from_project_home} && git push -u origin {git_published_branch}')

    if git_merged_branch is not None and git_merged_branch != '':
        output_std(f'>>> 切换到待合并到的分支: {git_merged_branch}')
        os.system(f'cd {from_project_home} && git checkout {git_merged_branch}')
        output_strict(f'>>> 切换到待合并到的分支: {git_merged_branch}', resp)
        resp = os.system(
            f'cd {from_project_home} && git merge {git_published_branch} && git push -u origin {git_merged_branch}')
        output_strict(f'<<< 合并到远程分支: {git_merged_branch}', resp)

    if git_tag_version is not None and git_tag_version != '' and git_tag_comment is not None and git_tag_comment != '':
        output_std(f'>>> 打标签名：{git_tag_version}，注释：{git_tag_comment}')
        resp = os.system(f'cd {from_project_home} && git tag -a {git_tag_version} -m {git_tag_comment} && git push -u origin {git_tag_version}')
        output_relaxed(f'<<< 打标签名：{git_tag_version}，注释：{git_tag_comment}', resp)

    if git_delete_temp_branch is not None and git_delete_temp_branch != '' \
            and generated_timestamped_branch is not None and generated_timestamped_branch != '':
        output_std(f'>>> 删除远程临时分支：{generated_timestamped_branch}')
        resp = os.system(f'cd {from_project_home} && git push origin --delete {generated_timestamped_branch}')
        output_relaxed(f'<<< 删除远程临时分支：{generated_timestamped_branch}', resp)

    output_std('<<<<<<<<<< 发布流程执行结束!! >>>>>>>>>>')

    return 'PUBLISH OVER'


if __name__ == '__main__':
    # define variables
    git_repo = git_branches = project_name = profile = source_file_dir = to_ip = to_project_home = to_process_name = \
        to_java_opts = git_merged_branch = git_tag_version = git_tag_comment = git_delete_temp_branch = None

    # receive parameters
    opts = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hwh:gr:gb:pn:pf:sfd:ti:tph:tpn:tj:gmb:gtv:gtc:gdtb",
                                   ["help", "work_home=", "git_repo=", "git_branches=", "project_name=", "profile=",
                                    "source_file_dir=",
                                    "to_ip=", "to_project_home=", "to_process_name=", "to_java_opts=",
                                    "git_merged_branch=", "git_tag_version=", "git_tag_comment=",
                                    "git_delete_temp_branch="])
    except getopt.GetoptError as e:
        output_error(f'getopt error: {e.msg}')

    # extract parameters
    for opt, arg in opts:
        if opt == '-h':
            output_std('Usage to see the source file')
        elif opt in ("--work_home", "-wh"):
            work_home = arg
        elif opt in ("--git_repo", "-gr"):
            git_repo = arg
        elif opt in ("--git_branches", "-gb"):
            git_branches = arg
        elif opt in ("--project_name", "-pn"):
            project_name = arg
        elif opt in ("--profile", "-pf"):
            profile = arg
        elif opt in ("--source_file_dir", "-sfd"):
            source_file_dir = arg
        elif opt in ("--to_ip", "-ti"):
            to_ip = arg
        elif opt in ("--to_project_home", "-tph"):
            to_project_home = arg
        elif opt in ("--to_process_name", "-tpn"):
            to_process_name = arg
        elif opt in ("--to_java_opts", "tj"):
            to_java_opts = arg
        elif opt in ("--git_merged_branch", "-gmb"):
            git_merged_branch = arg
        elif opt in ("--git_tag_version", "-gtv"):
            git_tag_version = arg
        elif opt in ("--git_tag_comment", "-gtc"):
            git_tag_comment = arg
        elif opt in ("--git_delete_temp_branch", "-gdtb"):
            git_delete_temp_branch = arg

    # invoke publish function
    publish(git_repo, git_branches, project_name, profile, source_file_dir, to_ip, to_project_home, to_process_name,
            to_java_opts, git_merged_branch, git_tag_version, git_tag_comment, git_delete_temp_branch)
