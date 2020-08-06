#!/usr/bin/env python3
# usage: python3 [script].py  [--git_repo=] [--git_branches=] [--project_name=] [--profile=] [--to_username=] [--to_ip=] [--to_project_home=]
# eg: python3 devops_nodejs.py --git_repo=git@192.168.1.248:2019_lx_group/spark_BMS.git --git_branches=master --project_name=spark_BMS --profile=dev --to_username=root --to_ip=192.168.1.248 --to_project_home=/home/project/mama_docs

import configparser
import getopt
import sys
import os

sys.path.append(os.path.realpath('.'))
from src.utils.sshcmd import scp_cmd, ssh_cmd
from src.scripts.output import output_all, output_error, output_relaxed, output_std, output_strict, output_warn

# global variables
work_home = None
server_passport_config_location = 'src/configs/server_passport.cfg'


def publish(git_repo, git_branch, project_name, profile, to_ip, to_project_home, to_process_port):
    # verify parameters
    # TODO or not profile \
    if not git_repo or not git_branch \
            or not project_name \
            or not to_ip \
            or not to_project_home:
        output_error(
            f'required parameters cannot be empty: git_repo:{git_repo}, git_branches:{git_branches}, '
            f'project_name:{project_name}, profile:{profile}, to_ip:{to_ip}, to_project_home:{to_project_home}')

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
    resp = os.system(f'cd {work_home} && git clone {git_repo} -b {git_branch} --depth=1')
    output_strict('<<< 克隆项目到发布系统本地', resp)

    output_std('>>> npm构建开始')
    resp = os.system(f'cd {from_project_home} && cnpm run build')
    output_strict('<<< npm构建结束', resp)

    # TODO
    file_path = f'{from_project_home}/'

    output_std(f'>>> SCP远程上传文件，from_folder_path：{file_path}，to_folder_path：{to_project_home}')
    scp_result = scp_cmd(to_ip, to_password, file_path, to_project_home, to_username)
    output_std(f'<<< SCP远程上传文件结束，状态：{scp_result}')

    output_std('>>> SSH远程执行命令开始...')
    ssh_cmd_result = ssh_cmd(to_ip, to_password,
                             [f'sh /home/devops/restart_nodejs.sh {to_project_home} {to_process_port}'],
                             to_username)
    output_std(f'<<< SSH远程执行命令结束，状态：{ssh_cmd_result}')
    if ssh_cmd_result != 0:
        output_error('SSH远程执行命令失败！')


if __name__ == '__main__':
    # define variables
    git_repo = git_branches = project_name = profile = source_file_dir = to_ip = to_project_home = None

    # receive parameters
    opts = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hwh:gr:gb:pn:pf:sfd:ti:tph",
                                   ["help", "work_home=", "git_repo=", "git_branches=", "project_name=", "profile=",
                                    "source_file_dir=", "to_ip=",
                                    "to_project_home="])
    except getopt.GetoptError as e:
        output_error(f'getopt error: {e.msg}')

    # extract parameters
    for opt, arg in opts:
        if opt == '-h':
            print('Usage to see the source file')
            exit()
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

    # invoke publish function
    publish(git_repo, git_branches, project_name, profile, to_ip, to_project_home, to_process_port=3002)  # TODO
