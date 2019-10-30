#!/usr/bin/env python3
import os
import sys
import time
import subprocess
from sshcmd import *
import getopt


def output_all(resp, error_msg='发布失败，请稍后重试', success_msg=None):
    if resp != 0:
        print(error_msg)
        exit(1)
    () if (success_msg is None) else print(success_msg)


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
    print("------------aaaaaa-------------")
    resp = os.system(f'cd {work_home} && rm -rf {project_name}')
    output_all(resp)
    print("------------bbbbbb-------------")
    resp = os.system(f'cd {work_home} && git clone -b {place_holder_branch} {git_repo}')
    output_all(resp)
    print("------------ccccccc-------------")
    generated_timestamped_branch = ''
    if not is_standalone_branch:
        generated_timestamped_branch = "temp-" + time.strftime("%Y%m%d%H%M%S", time.localtime())
        resp = os.system(f'cd {from_project_home} && git checkout -b {generated_timestamped_branch}')
        output_all(resp)
        for each_branch in git_branches_array:
            resp = os.system(f'cd {from_project_home} && git merge {each_branch}')
            output_all(resp)
    print("------------dddddddd-------------")
    resp = os.system(f'cd {from_project_home} && mvn clean package -Dmaven.test.skip=true -P {profile} -U')
    output_all(resp)
    print("------------eeeeeee-------------")
    (status, output) = subprocess.getstatusoutput(f'ls {from_project_home}/target/*.*ar')
    print("------------1111-------------")
    print("-------------111------------")
    scp_cmd(to_ip, 'zhimore123', output, f'{to_project_home}/web/', f'{to_username}')

    output_all(resp)
    print("--------------2222-----------")
    print("---------------22222----------")

    ssh_cmd(to_ip, 'zhimore123',
            [f'sh /home/devops/restart_jar.sh {to_project_home} {to_process_name} "{to_java_opts}"'],
            to_username)

    if not git_merged_branch and git_merged_branch is not None:
        os.system(f'cd {from_project_home} && git checkout {git_merged_branch}')
        if not is_standalone_branch:
            resp = os.system(f'cd {from_project_home} && git merge {generated_timestamped_branch}')
        else:
            resp = os.system(f'cd {from_project_home} && git merge {git_branches_array[0]}')
        output_all(resp)

    if not git_tag_version and git_tag_version is not None and not git_tag_comment and git_tag_comment is not None:
        resp = os.system(f'git tag -a {git_tag_version} -m {git_tag_comment}')
        output_all(resp)

    if not git_delete_temp_branch and git_delete_temp_branch is not None and generated_timestamped_branch != '' and generated_timestamped_branch is not None:
        resp = os.system(f'git push origin --delete {generated_timestamped_branch}')
        output_all(resp)

    return 'PUBLISH SUCCESS'


if __name__ == '__main__':
    git_repo, git_branches, project_name, profile, to_username, to_ip, to_project_home, to_process_name, to_java_opts, \
    git_merged_branch, git_tag_version, git_tag_comment, git_delete_temp_branch = None, None, None, None, None, None, None, None, None, None, None, None, None
    # receive parameters
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hgr:gb:pn:pf:tu:ti:tph:tpn:tj:gmb:gtv:gtc:gdtb",
                                   ["help", "git_repo=", "git_branches=", "project_name=", "profile=", "to_username=",
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

    publish(git_repo, git_branches, project_name, profile, to_username, to_ip, to_project_home, to_process_name,
            to_java_opts, git_merged_branch, git_tag_version, git_tag_comment, git_delete_temp_branch)
