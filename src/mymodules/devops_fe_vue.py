#!/usr/bin/env python3
# usage: python3 [script].py  [--git_repo=] [--git_branches=] [--project_name=] [--profile=] [--to_username=] [--to_ip=] [--to_project_home=]
# eg: python3 devops_fe_vue.py --git_repo=git@192.168.1.248:2019_lx_group/spark_BMS.git --git_branches=master --project_name=spark_BMS --profile=dev --to_username=root --to_ip=192.168.1.248 --to_project_home=/home/project/mama_docs

import getopt
import sys
import os

try:
    from sshcmd import scp_cmd, ssh_cmd
except:
    print('import error, try another path..')
    sys.path.append(os.path.realpath('.'))
    from src.mymodules.sshcmd import scp_cmd, ssh_cmd


def output_all(resp, info_msg=None, error_msg='发布失败，请稍后重试'):
    () if (info_msg is None) else print(info_msg)
    if resp != 0:
        print(error_msg)
        exit(1)
    sys.stdout.flush()


def publish(git_repo, git_branch, project_name, to_username, to_ip, to_project_home,
            work_home="/Users/wangnan/workspace/github/devops-py/devopstemp/"):
    # verify parameters
    if not git_repo or not git_branch \
            or not project_name \
            or not to_username \
            or not to_ip \
            or not to_project_home:
        print('ERROR: required parameters cannot be empty')
        sys.exit()

    from_project_home = work_home + project_name
    req = 0

    output_all(req, '>>> 清除历史项目痕迹，开始新的工作')
    resp = os.system(f'cd {work_home} && rm -rf {project_name}')
    print(f'{work_home}, {project_name}')
    output_all(resp, '<<< 清除历史项目痕迹，开始新的工作')

    output_all(req, '>>> 克隆项目到发布系统本地')
    resp = os.system(f'cd {work_home} && git clone -b {git_branch} {git_repo}')
    output_all(resp, '<<< 克隆项目到发布系统本地')

    output_all(req, f'>>> npm构建开始')
    resp = os.system(f'cd {from_project_home} && npm install && npm run test')
    output_all(resp, f'<<< npm构建结束')

    file_path = f'{from_project_home}/dist'

    output_all(0, f'>>> SCP远程上传文件开始...')
    scp_result = scp_cmd(to_ip, 'zhimore123', file_path, f'{to_project_home}/web/', f'{to_username}')
    output_all(0, f'<<< SCP上传文件结束，状态：{scp_result}')


if __name__ == '__main__':
    # define variables
    git_repo = git_branches = project_name = to_username = to_ip = to_project_home = None

    # receive parameters
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hgr:gb:pn:pf:tu:ti:tph",
                                   ["help", "git_repo=", "git_branches=", "project_name=", "profile=",
                                    "to_username=", "to_ip=", "to_project_home="])
    except getopt.GetoptError as e:
        print("getopt error,", e)
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

    # invoke publish function
    publish(git_repo, git_branches, project_name, to_username, to_ip, to_project_home)
