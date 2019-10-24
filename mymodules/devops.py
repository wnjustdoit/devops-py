#!/usr/bin/env python3
import os
import sys
import time
import subprocess
from .sshcmd import *


def output_all(resp, error_msg='发布失败，请稍后重试', success_msg=None):
    if resp != 0:
        print(error_msg)
        exit(1)
    () if (success_msg is None) else print(success_msg)


def publish(git_repo, git_branches, project_name, profile, to_username, to_ip, to_project_home, to_process_name,
            to_java_opts,
            git_merged_branch, git_tag_version, git_tag_comment, git_delete_temp_branch,
            work_home="~/workspace/newlanguage/python/work/devops/"):
    # declare extra parameters
    is_standalone_branch = True
    git_branches_array = ()
    place_holder_branch = ""

    # verify parameters
    if not git_repo.strip() or len(git_branches) == 0 \
            or not project_name.strip() \
            or not profile.strip() \
            or not to_username.strip() \
            or not to_ip.strip() \
            or not to_project_home.strip() \
            or not to_process_name.strip():
        print('ERROR: required parameters cannot be empty')
        sys.exit()

    if len(git_branches) > 1:
        is_standalone_branch = False
        git_branches_array = git_branches
        filter(None, git_branches_array)
        if len(git_branches_array) == 0:
            print('parameter [git_branches] invalid')
            sys.exit()
        place_holder_branch = git_branches_array[0]
    else:
        place_holder_branch = git_branches[0]

    from_project_home = work_home + project_name

    resp = os.system(f'cd {work_home} && rm -rf {project_name}')
    output_all(resp)
    resp = os.system(f'cd {work_home} && git clone -b {place_holder_branch} {git_repo}')
    output_all(resp)
    generated_timestamped_branch = ''
    if not is_standalone_branch:
        generated_timestamped_branch = "temp-" + time.strftime("%Y%m%d%H%M%S", time.localtime())
        resp = os.system(f'cd {from_project_home} && git checkout -b {generated_timestamped_branch}')
        for each_branch in git_branches_array:
            resp = os.system(f'cd {from_project_home} && git merge {each_branch}')

    resp = os.system(f'cd {from_project_home} && mvn clean package -Dmaven.test.skip=true -P {profile} -U')
    output_all(resp)
    (status, output) = subprocess.getstatusoutput(f'ls {from_project_home}/target/*.*ar')
    scp_cmd(to_ip, 'zhimore123', output, f'{to_project_home}/web/', f'{to_username}')

    output_all(resp)

    ssh_cmd(to_ip, 'zhimore123',
            [f'sh /home/devops/restart_jar.sh {to_project_home} {to_process_name} "{to_java_opts}"'],
            to_username)

    if not git_merged_branch.strip():
        os.system(f'cd {from_project_home} && git checkout {git_merged_branch}')
        if not is_standalone_branch:
            resp = os.system(f'cd {from_project_home} && git merge {generated_timestamped_branch}')
        else:
            resp = os.system(f'cd {from_project_home} && git merge {git_branches[0]}')

    if not git_tag_version and not git_tag_comment:
        resp = os.system(f'git tag -a {git_tag_version} -m {git_tag_comment}')

    if git_delete_temp_branch and generated_timestamped_branch != '':
        resp = os.system(f'git push origin --delete {generated_timestamped_branch}')

    return 'PUBLISH SUCCESS'
