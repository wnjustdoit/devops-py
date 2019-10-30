#!/usr/bin/env python3
import os
import sys
import time
import subprocess
import getopt

sys.path.append(os.path.realpath('.'))
from src.mymodules.sshcmd import scp_cmd, ssh_cmd


def output_all(resp, info_msg=None, error_msg='发布失败，请稍后重试'):
    () if (info_msg is None) else print(info_msg)
    if resp != 0:
        print(error_msg)
        exit(1)
    sys.stdout.flush()


def publish(git_repo, git_branches, project_name, profile, to_username, to_ip, to_project_home, to_process_name,
            to_java_opts,
            git_merged_branch, git_tag_version, git_tag_comment, git_delete_temp_branch,
            work_home="~/workspace/github/devops-py/devopstemp/"):
    # declare extra parameters
    is_standalone_branch = True
    git_branches_array = git_branches.split(',')

    # verify parameters
    if not git_repo or len(git_branches_array) == 0 \
            or not project_name \
            or not profile \
            or not to_username \
            or not to_ip \
            or not to_project_home \
            or not to_process_name:
        print('ERROR: required parameters cannot be empty')
        sys.exit()

    if len(git_branches_array) > 1:
        is_standalone_branch = False
        filter(None, git_branches_array)
        if len(git_branches_array) == 0:
            print('parameter [git_branches] invalid')
            sys.exit()
        place_holder_branch = git_branches_array[0]
    else:
        place_holder_branch = git_branches_array[0]

    from_project_home = work_home + project_name
    req = 0

    output_all(req, '>>> 清除历史项目痕迹，开始新的工作')
    resp = os.system(f'cd {work_home} && rm -rf {project_name}')
    output_all(resp, '<<< 清除历史项目痕迹，开始新的工作')

    output_all(req, '>>> 克隆项目到发布系统本地')
    resp = os.system(f'cd {work_home} && git clone -b {place_holder_branch} {git_repo}')
    output_all(resp, '<<< 克隆项目到发布系统本地')

    generated_timestamped_branch = ''
    if not is_standalone_branch:
        generated_timestamped_branch = "temp-" + time.strftime("%Y%m%d%H%M%S", time.localtime())
        output_all(req, f'>>> 创建临时分支{generated_timestamped_branch}，并切到新分支上')
        resp = os.system(f'cd {from_project_home} && git checkout -b {generated_timestamped_branch}')
        output_all(resp, f'<<< 创建临时分支{generated_timestamped_branch}，并切到新分支上')
        for each_branch in git_branches_array:
            output_all(req, f'>>> 在新分支上合并分支{each_branch}')
            resp = os.system(f'cd {from_project_home} && git merge {each_branch}')
            output_all(resp, f'<<< 在新分支上合并分支{each_branch}')

    output_all(resp, f'>>> maven打包结束，打包环境：{profile}')
    resp = os.system(f'cd {from_project_home} && mvn clean package -Dmaven.test.skip=true -P {profile} -U')
    output_all(resp, f'<<< maven打包结束，打包环境：{profile}')

    (status, filepath) = subprocess.getstatusoutput(f'ls {from_project_home}/target/*.*ar')
    output_all(0, f'>>> SCP远程上传文件开始...')
    scp_result = scp_cmd(to_ip, 'zhimore123', filepath, f'{to_project_home}/web/', f'{to_username}')
    output_all(0, f'<<< SCP上传文件结束，状态：{scp_result}')

    output_all(0, f'>>> 远程执行命令开始...')
    ssh_cmd_result = ssh_cmd(to_ip, 'zhimore123',
                             [f'sh /home/devops/restart_jar.sh {to_project_home} {to_process_name} "{to_java_opts}"'],
                             to_username)
    output_all(0, f'<<< 远程执行命令结束，状态：{ssh_cmd_result}')

    if git_merged_branch is not None and git_merged_branch != '':
        os.system(f'cd {from_project_home} && git checkout {git_merged_branch}')
        output_all(req, f'>>> 合并到分支{git_merged_branch}')
        if not is_standalone_branch:
            resp = os.system(f'cd {from_project_home} && git merge {generated_timestamped_branch}')
        else:
            resp = os.system(f'cd {from_project_home} && git merge {git_branches_array[0]}')
        output_all(resp, f'<<< 合并到分支{git_merged_branch}')

    if git_tag_version is not None and git_tag_version != '' and git_tag_comment is not None and git_tag_comment != '':
        output_all(req, f'>>> 打标签名：{git_tag_version}，注释：{git_tag_comment}')
        resp = os.system(f'git tag -a {git_tag_version} -m {git_tag_comment}')
        output_all(resp, f'<<< 打标签名：{git_tag_version}，注释：{git_tag_comment}')

    if git_delete_temp_branch is not None and git_delete_temp_branch != '' and generated_timestamped_branch is not None and generated_timestamped_branch != '':
        output_all(req, f'>>> 删除远程临时分支：{generated_timestamped_branch}')
        resp = os.system(f'git push origin --delete {generated_timestamped_branch}')
        output_all(resp, f'<<< 删除远程临时分支：{generated_timestamped_branch}')

    output_all(0, '<<<<<<<<<< 发布流程执行结束!! >>>>>>>>>>')

    return 'PUBLISH OVER'


if __name__ == '__main__':
    # define variables
    git_repo, git_branches, project_name, profile, to_username, to_ip, to_project_home, to_process_name, \
    to_java_opts, git_merged_branch, git_tag_version, git_tag_comment, git_delete_temp_branch \
        = None, None, None, None, None, None, None, None, None, None, None, None, None

    # receive parameters
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hgr:gb:pn:pf:tu:ti:tph:tpn:tj:gmb:gtv:gtc:gdtb",
                                   ["help", "git_repo=", "git_branches=", "project_name=", "profile=",
                                    "to_username=",
                                    "to_ip=", "to_project_home=", "to_process_name=", "to_java_opts=",
                                    "git_merged_branch=", "git_tag_version=", "git_tag_comment=",
                                    "git_delete_temp_branch="])
    except getopt.GetoptError:
        print("getopt error")
        sys.exit(2)

    # extract parameters
    for opt, arg in opts:
        if opt == '-h':
            print('Usage to see the source file')
            exit()
        elif opt in ("--git_repo", "-gr"):
            git_repo = arg
        elif opt in ("--git_branches", "-gb"):
            git_branches = arg
        elif opt in ("--project_name", "-pn"):
            project_name = arg
        elif opt in ("--profile", "-pf"):
            profile = arg
        elif opt in ("--to_username", "-tu"):
            to_username = arg
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
    publish(git_repo, git_branches, project_name, profile, to_username, to_ip, to_project_home, to_process_name,
            to_java_opts, git_merged_branch, git_tag_version, git_tag_comment, git_delete_temp_branch)
