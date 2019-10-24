#!/usr/bin/env python3
# http://git.mamaqunaer.cc/api/v3/projects?private_token=LTDbr3zzJza_JwC8_Gjz
import gitlab

import os
import sys


class GitlabAPI(object):
    def __init__(self, *args, **kwargs):
        if os.path.exists('/etc/python-gitlab.cfg'):
            self.gl = gitlab.Gitlab.from_config('mamaqunaer', ['/etc/python-gitlab.cfg'])
        elif os.path.exists(os.getenv('HOME') + '/.python-gitlab.cfg'):
            self.gl = gitlab.Gitlab.from_config('mamaqunaer', [os.getenv('HOME') + '/.python-gitlab.cfg'])
        else:
            print('You need to make sure there is a file named "/etc/python-gitlab.cfg" or "~/.python-gitlab.cfg"')
            sys.exit(5)

    def get_user_id(self, username):
        user = self.gl.users.get_by_username(username)
        return user.id

    def get_group_id(self, groupname):
        group = self.gl.users.search(groupname)
        return group[0].id

    def get_all_projects(self):
        projects = self.gl.projects.list(all=True)
        result_list = []
        for project in projects:
            result_list.append({'id': project.id, 'name': project.name, 'ssh_url_to_repo': project.ssh_url_to_repo,
                                'http_url_to_repo': project.http_url_to_repo, 'description': project.description,
                                'web_url': project.web_url, 'name_with_namespace': project.name_with_namespace,
                                'path': project.path,
                                'path_with_namespace': project.path_with_namespace})
        return result_list

    def get_user_projects(self, userid):
        projects = self.gl.projects.owned(userid=userid, all=True)
        result_list = []
        for project in projects:
            result_list.append(project.http_url_to_repo)
        return result_list

    def get_group_projects(self, groupname):
        projects = self.gl.projects.owned(groupname=groupname, all=True)
        result_list = []
        for project in projects:
            result_list.append(project.http_url_to_repo)
        return result_list

    def get_project_repo(self, projectid):
        return self.gl.projects.get(projectid).ssh_url_to_repo

    def get_project_name(self, projectid):
        return self.gl.projects.get(projectid).name

    def get_project_branches(self, projectid):
        branches = self.gl.projects.get(projectid).branches.list()
        result_list = []
        print(branches)
        for branch in branches:
            result_list.append(branch.name)
        return result_list

# if __name__ == '__main__':
#     username = 'wangnan'
#     git = GitlabAPI()
#     userid = git.get_user_id(username)
#     print(username + '->' + str(userid))
#     userprojects = git.get_user_projects(userid)
#     print(userprojects)
