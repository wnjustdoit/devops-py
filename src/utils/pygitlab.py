#!/usr/bin/env python3
# module "python-gitlab"
import gitlab

import os
import sys


class GitlabAPI(object):
    def __init__(self, *args, **kwargs):
        if os.path.exists('/etc/python-gitlab.cfg'):
            self.gl = gitlab.Gitlab.from_config('mamaqunaer', ['/etc/python-gitlab.cfg'])
        elif os.path.exists(os.getenv('HOME') + '/.python-gitlab.cfg'):
            self.gl = gitlab.Gitlab.from_config('mamaqunaer', [os.getenv('HOME') + '/.python-gitlab.cfg'])
        elif os.path.exists(os.path.realpath('.') + '/src/configs/python-gitlab.cfg'):
            self.gl = gitlab.Gitlab.from_config('mamaqunaer',
                                                [os.path.realpath('.') + '/src/configs/python-gitlab.cfg'])
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
        for branch in branches:
            result_list.append(branch.name)
        return result_list

    def get_project_tags(self, projectid):
        tags = self.gl.projects.get(projectid).tags.list()
        result_list = []
        for tag in tags:
            result_list.append(tag.name)
        return result_list

    def get_project_commits(self, projectid):
        commits = self.gl.projects.get(projectid).commits.list()
        result_list = []
        for commit in commits:
            result_list.append(commit.id)
        return result_list


if __name__ == "__main__":
    # GitlabAPI().gl.projects.get(174).hooks.create(
    #     {'url': 'http://192.168.1.248:5000/web_hook/publish', 'push_events': True, 'tag_push_events': True, 'note_events': True})
    print(GitlabAPI().gl.projects.get(174).hooks.list())
    # for hook in GitlabAPI().gl.projects.get(174).hooks.list():
    #     hook.delete()
