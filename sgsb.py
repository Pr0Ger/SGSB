#!/usr/bin/env python3

import argparse
import configparser
import dropbox
import os
from lib import plugins
from lib import win_console

parser = argparse.ArgumentParser(description='Simple game saves backup tool.')
Tasks = parser.add_argument_group('Tasks')
Tasks.add_argument('tasks', metavar='TASK', action='append', choices=['auth', 'list', 'backup', 'restore'])
Tasks.add_argument('--all', action='store_true', help="Ignore task.ini and perform task for all available games")

args = parser.parse_args()

plugins.LoadPlugins()

for task in args.tasks:
    if task == "auth":
        from lib.dropbox import app_key, app_secret

        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

        authorize_url = flow.start()
        print('1. Go to: ' + authorize_url)
        print('2. Click "Allow" (you might have to log in first)')
        print('3. Copy the authorization code.')
        print("Enter the authorization code here: ", end='')
        code = input().strip()  # Using input with argument produce error on windows

        access_token, user_id = flow.finish(code)

        access_file = open('.dropbox_access_token', 'w')
        access_file.write(access_token)
        access_file.close()

    if task == "list":
        backups_dropbox = []

        if os.path.exists('.dropbox_access_token'):
            access_file = open('.dropbox_access_token', 'r')
            access_token = access_file.read()
            dropbox_client = dropbox.client.DropboxClient(access_token)

            root_folder = dropbox_client.metadata('/')
            for it in root_folder['contents']:
                backups_dropbox.append(it['path'][1:])

        def check_exists(file_name):
            storage_name = file_name + '.tar.xz'

            if storage_name in backups_dropbox:
                return True
            if os.path.exists(os.path.join('.', 'backups', storage_name)):
                return True

            return False

        print()
        print('+-------------------------------------------------------+-----------+----------+')
        print('| Name                                                  | Installed | Backuped |')
        print('+-------------------------------------------------------+-----------+----------+')

        for name in sorted(plugins.plugins_list):
            it = plugins.plugins_list[name]
            restricted_characters = '/\\?%*:|"<>'
            file_name = ''.join(filter(lambda x: x not in restricted_characters, it.Name))
            if it.available:
                name = it.Name[:50] + '...' if len(it.Name) > 53 else it.Name
            else:
                name = it.Name[:34] + '... (Not available)' if (len(it.Name) > 37) else it.Name

            installed = '+' if it.available and it.detect() else ' '
            backuped = '+' if check_exists(file_name) else ' '

            print('| %-53s |     %s     |    %s     |' % (name, installed, backuped))

        print('+-------------------------------------------------------+-----------+----------+')

    if task == "backup" or task == "restore":

        def perform_task(name, task):
            plugin = plugins.plugins_list[name]
            if plugin.available:
                for dep in plugin.dependencies:
                    if dep in task_order:
                        try:
                            perform_task(dep, task)
                        except IOError:
                            print("WARN: Plugin '{}' require broken '{}' plugin.".format(plugin.Name, dep))
                        task_order.remove(dep)

                print()
                getattr(plugin, task)()
            else:
                print('')
                print('Game {} isn\'t supported on your current platform...'.format(plugin.Name))

        if not args.all:
            task_order = set()

            task_reader = configparser.ConfigParser()
            task_reader.read('task.ini')
            for it in task_reader.sections():
                if task_reader.getboolean(it, task):
                    task_order.add(it)

                    if not it in plugins.plugins_list:
                        print("WARN: Required plugin '{} doen't exists.".format(it))
                    else:
                        for dep in plugins.plugins_list[it].dependencies:
                            task_order.add(dep)
        else:
            task_order = set(plugins.plugins_list.keys())

        while task_order:
            try:
                perform_task(task_order.pop(), task)
            except IOError:
                pass
