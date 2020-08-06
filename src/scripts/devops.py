#!/usr/bin/env python3
# usage: python3 [script.py] [--work_home=] [--git_repo=] [--git_branches=] [--project_name=] [--profile=] [--source_file_dir=] [--to_ip=] [--to_project_home=] [--to_process_name=] [--to_java_opts=] [--git_merged_branch=] [--git_tag_version=] [--git_tag_comment=] [--git_delete_temp_branch=] [--docker=]
# eg: python3 src/scripts/devops.py --work_home=/tmp/devops --git_repo=git@192.168.1.248:mall/config-server.git --git_branches=develop --project_name=config-server --profile=dev --source_file_dir=target --to_ip=192.168.1.248 --to_project_home=/home/project/mama_config_server --to_process_name=config-server --to_java_opts="-Xms256m -Xmx768m" --git_merged_branch= --git_tag_version= --git_tag_comment= --git_delete_temp_branch=0 --docker=1 --server_port=8088
# 约定1：远程执行脚本路径（工程见devops-sh）：/home/devops/restart_*ar.sh
# 约定2：打包完毕上传至远程服务器目录：[path_to_project_home]/web/；远程服务器项目备份目录：[path_to_project_home]/backup/。如果目录不存在，会自动创建。
# 其他：如果作为Python脚本脱离web容器独立运行的话，注意引入其他模块或配置文件的路径；
# 多分支发布时，临时分支命名格式：publish-temp-{%Y%m%d%H%M%S}

import os
import sys
import time
import subprocess
import getopt
import configparser

sys.path.append(os.path.realpath('.'))
from src.utils.sshcmd import scp_cmd, ssh_cmd
from src.scripts.output import output_all, output_error, output_relaxed, output_std, output_strict, output_warn

# global variables
# default devops work home
work_home: str = '/tmp/devops'

# server password file location
server_passport_config_location = 'src/configs/server_passport.cfg'

# default tomcat dir name
to_tomcat_dir_name = 'apache-tomcat-8.5.23'


def publish(git_repo: str, git_branches: str, project_name: str, profile: str, source_file_dir: str, to_ip: str,
            to_project_home: str,
            to_process_name: str,
            to_java_opts: str, git_merged_branch: str, git_tag_version: str, git_tag_comment: str,
            git_delete_temp_branch, docker,
            server_port: int):
    # declare extra parameters
    is_standalone_branch = True
    git_branches_array = git_branches.split(',')

    # verify parameters
    if git_repo is None or git_repo.strip() == '' \
            or len(git_branches_array) == 0 \
            or profile is None or profile.strip() == '' \
            or to_ip is None or to_ip.strip() == '' \
            or to_project_home is None or to_project_home.strip() == '' \
            or to_process_name is None or to_process_name.strip() == '':
        output_error(
            f'required parameters cannot be empty: git_repo:{git_repo}, git_branches:{git_branches}, '
            f'project_name:{project_name}, profile:{profile}, to_ip:{to_ip}, to_project_home:{to_project_home}, to_process_name:{to_process_name}')

    # handle the branch(es)
    if len(git_branches_array) > 1:
        is_standalone_branch = False
        filter(None, git_branches_array)
        if len(git_branches_array) == 0:
            output_error('parameter [git_branches] invalid')

    place_holder_branch = git_branches_array[0]

    # read config.properties
    config = configparser.ConfigParser()
    config.read(server_passport_config_location)
    to_username = config.get(to_ip, 'username')
    to_password = config.get(to_ip, 'password')

    # project name, if empty, substr from the git repo
    if project_name is None or project_name.strip() == '':
        project_name = git_repo[git_repo.rindex('/') + 1:git_repo.rindex('.')]

    # local project home
    from_project_home = work_home + ('/' if not work_home.endswith('/') else '') + project_name

    # to project home
    to_project_home = (to_project_home if not to_project_home.endswith('/') else to_project_home.rstrip('/'))

    # source file dir
    source_file_dir = (source_file_dir if not source_file_dir.endswith('/') else source_file_dir.rstrip('/'))

    output_std(f'>>> 清除历史项目痕迹，开始新的工作work_home:{work_home} [$step0]')
    resp = os.system(f'cd {work_home} && rm -rf {project_name}')
    output_strict('<<< 清除历史项目痕迹，开始新的工作', resp)

    output_std('>>> 克隆项目到发布系统本地 [$step1]')
    resp = os.system(f'cd {work_home} && git clone {git_repo} -b {place_holder_branch}'
                     + (' --depth=1' if is_standalone_branch else '')  # 不是多分支时才浅克隆
                     + f' "./{project_name}"')  # 克隆到项目名称文件夹下（不存在会自动创建）
    output_strict('<<< 克隆项目到发布系统本地', resp)

    # when multiple branches
    generated_timestamped_branch = ''
    if not is_standalone_branch:
        # temporary branch generated strategy(when multiple branches)
        generated_timestamped_branch = "devops-temp-" + time.strftime("%Y%m%d%H%M%S", time.localtime())
        output_std(f'>>> 创建临时分支{generated_timestamped_branch}，并切到新分支上')
        resp = os.system(f'cd {from_project_home} && git checkout -b {generated_timestamped_branch}')
        output_strict(f'<<< 创建临时分支{generated_timestamped_branch}，并切到新分支上', resp)
        for each_branch in git_branches_array:
            output_std(f'>>> 在新分支上合并分支{each_branch}')
            resp = os.system(f'cd {from_project_home} && git merge origin/{each_branch}')
            # ignore 256: "merge: {branch} - not something we can merge  Did you mean this?"
            output_strict(f'<<< 在新分支上合并分支{each_branch}', resp if resp != 256 else 0)

    output_std(f'>>> maven打包开始，打包环境：{profile} [$step2]')
    resp = os.system(f'cd {from_project_home} && mvn clean package -Dmaven.test.skip=true -P {profile} -U')
    output_strict(f'<<< maven打包结束，打包环境：{profile}', resp)

    # lookup local file location
    output_std(f'>>> 检查本地*ar包是否生成，目录路径：{from_project_home}/{source_file_dir} [$step3]')
    (status, file_path) = subprocess.getstatusoutput(f'ls {from_project_home}/{source_file_dir}/*.*ar')
    source_file_type = file_path[file_path.rindex('.') + 1:]
    source_file_name = file_path[file_path.rindex('/') + 1:file_path.rindex('.')]
    output_strict(f'<<< 检查本地{source_file_type}包生成结果，文件路径：{file_path}', status)

    # if docker env or not
    repository = f'registry.cn-hangzhou.aliyuncs.com/mamaqunaer/mama:{profile}-{source_file_name}'
    if docker is None or docker == '' or docker == 0 or docker == '0':
        # check if remote folders exist or create ones forcibly
        output_std(f'>>> SSH远程检查文件夹是否存在（不存在则创建），目标目录：{to_project_home}/web，备份目录：{to_project_home}/backup')
        ssh_cmd_result = ssh_cmd(to_ip, to_password,
                                 [
                                     f'if [ ! -d {to_project_home}/web ]; then mkdir -p {to_project_home}/web; fi '
                                     f'&& if [ ! -d {to_project_home}/backup ]; then mkdir -p {to_project_home}/backup; fi'],
                                 to_username)
        output_strict(f'<<< SSH远程检查文件夹是否存在，状态：{ssh_cmd_result}', ssh_cmd_result)

        output_std(f'>>> SCP远程上传文件，from_file_path：{file_path}，to_folder_path：{to_project_home}/web/ [$step4]')
        scp_result = scp_cmd(to_ip, to_password, file_path, f'{to_project_home}/web/', to_username)
        output_strict(f'<<< SCP远程上传文件结束，状态：{scp_result}', scp_result)
    else:
        # change current directory for docker context env
        os.chdir(from_project_home)
        # build Dockerfile
        fp = open('Dockerfile', 'w')
        output_std('>>> 当前为docker化工程，开始生成Dockerfile文件')
        try:
            fp.write('''\
                FROM openjdk:8-jdk-alpine
                VOLUME /tmp
                ENV TZ=Asia/Shanghai
                RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
                LABEL MAINTAINER="devops@mamaqunaer.com"
                ARG RELATIVE_JAR_FILE=target/*.jar
                COPY ${RELATIVE_JAR_FILE} app.jar
                ENTRYPOINT ["sh", "-c", "java ${JAVA_OPTS} -Djava.security.egd=file:/dev/./urandom -jar /app.jar"]''')
        finally:
            fp.close()
        # normally 'target/*.*ar'
        relative_jar_file = source_file_dir + '/' + source_file_name + "." + source_file_type
        output_std('>>> 开始执行docker build..')
        (status, output) = subprocess.getstatusoutput(
            f'docker build -t {repository} --build-arg RELATIVE_JAR_FILE={relative_jar_file} .')
        output_strict(output, status)
        output_std('>>> 开始执行docker push..')
        (status, output) = subprocess.getstatusoutput(f'docker push {repository}')
        output_strict(output, status)

    output_std('>>> SSH远程执行命令开始... [$step5]')
    # if docker env or not
    ssh_cmd_result = ''
    if docker is None or docker == '' or docker == '0':
        if source_file_type == 'jar':
            ssh_cmd_result = ssh_cmd(to_ip, to_password,
                                     [
                                         f'sh /home/devops/restart_jar.sh {to_project_home} {to_process_name} "{to_java_opts}"'],
                                     to_username)
        elif source_file_type == 'war':
            ssh_cmd_result = ssh_cmd(to_ip, to_password,
                                     [
                                         f'sh /home/devops/restart_war.sh {to_project_home} {to_process_name} {to_tomcat_dir_name}'],
                                     to_username)
        else:
            output_error(f'Unsupported source_file_type:{source_file_type}')
    else:
        output_std('>>> 开始远程执行docker stop & docker rm, 以及docker run命令..')
        ssh_cmd_result = ssh_cmd(to_ip, to_password,
                                 [
                                     "docker ps -a | grep " + project_name + " | awk '{print $1}' | xargs -r docker stop",
                                     "docker ps -a | grep " + project_name + " | awk '{print $1}' | xargs -r docker rm",
                                     "netstat -tunlp | grep " + str(
                                         server_port) + " | awk '{print $7}' | cut -d/ -f1 | xargs -r kill -9",
                                     f"docker run --name {project_name} -d -e \"JAVA_OPTS={to_java_opts}\" -p {server_port}:{server_port} -v {to_project_home}/logs:/logs {repository}"],
                                 to_username)
    output_strict(f'<<< SSH远程执行命令结束，状态：{ssh_cmd_result}', ssh_cmd_result)

    output_std('>>> 发布系统收尾工作.. [$step6]')

    # published branch
    if not is_standalone_branch:
        git_published_branch = generated_timestamped_branch
        output_std(f'>>> 推送当前发布分支：{git_published_branch}到远程')
        resp = os.system(
            f'cd {from_project_home} && git push -u origin {git_published_branch}')
        output_std(f'<<< 推送当前发布分支：{git_published_branch}到远程')
    else:
        git_published_branch = git_branches_array[0]

    # merge branches
    if git_merged_branch is not None and git_merged_branch != '':
        output_std(f'>>> 切换到待合并到的分支: {git_merged_branch}')
        os.system(f'cd {from_project_home} && git checkout {git_merged_branch}')
        output_strict(f'>>> 切换到待合并到的分支: {git_merged_branch}', resp)
        resp = os.system(
            f'cd {from_project_home} && git merge origin/{git_published_branch} && git push -u origin {git_merged_branch}')
        # ignore exception code 256: "not something we can merge"
        output_strict(f'<<< 合并到远程分支: {git_merged_branch}', resp if resp != 256 else 0)

    # git add tag
    if git_tag_version is not None and git_tag_version != '' and git_tag_comment is not None and git_tag_comment != '':
        output_std(f'>>> 打标签名：{git_tag_version}，注释：{git_tag_comment}')
        resp = os.system(
            f'cd {from_project_home} && git tag -a {git_tag_version} -m {git_tag_comment} && git push -u origin {git_tag_version}')
        output_relaxed(f'<<< 打标签名：{git_tag_version}，注释：{git_tag_comment}', resp)

    # whether to delete the temporary branch
    if git_delete_temp_branch is not None and git_delete_temp_branch != '' and git_delete_temp_branch != 0 \
            and generated_timestamped_branch is not None and generated_timestamped_branch != '':
        output_std(f'>>> 删除远程临时分支：{generated_timestamped_branch}')
        resp = os.system(f'cd {from_project_home} && git push origin --delete {generated_timestamped_branch}')
        output_relaxed(f'<<< 删除远程临时分支：{generated_timestamped_branch}', resp)

    output_std('<<<<<<<<<< 发布流程执行结束!! >>>>>>>>>> [$step7]')


if __name__ == '__main__':
    # define variables
    git_repo = git_branches = project_name = profile = source_file_dir = to_ip = to_project_home = to_process_name = \
        to_java_opts = git_merged_branch = git_tag_version = git_tag_comment = git_delete_temp_branch = docker = server_port = None

    # receive parameters
    opts = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hwh:gr:gb:pn:pf:sfd:ti:tph:tpn:tj:gmb:gtv:gtc:gdtb:dk:sp",
                                   ["help", "work_home=", "git_repo=", "git_branches=", "project_name=", "profile=",
                                    "source_file_dir=",
                                    "to_ip=", "to_project_home=", "to_process_name=", "to_java_opts=",
                                    "git_merged_branch=", "git_tag_version=", "git_tag_comment=",
                                    "git_delete_temp_branch=", "docker=", "server_port="])
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
        elif opt in ("--docker", "-dk"):
            docker = arg
        elif opt in ("--server_port", "-sp"):
            server_port = arg

    # invoke publish function
    publish(git_repo, git_branches, project_name, profile, source_file_dir, to_ip, to_project_home, to_process_name,
            to_java_opts, git_merged_branch, git_tag_version, git_tag_comment, git_delete_temp_branch, docker,
            server_port)
