#!/usr/bin/env python3

import argparse
import configparser
import os
from lib import plugins
from lib import win_console

parser = argparse.ArgumentParser(description='Simple game saves backup tool.')
Tasks = parser.add_argument_group('Tasks')
Tasks.add_argument('tasks', metavar='TASK', action='append', choices=['list', 'backup', 'restore'])
Tasks.add_argument('--all', action='store_true', help="Ignore task.ini and perform task for all available games")

args = parser.parse_args()

plugins.LoadPlugins()

for task in args.tasks:

    if task == "list":
        print()
        print('+-------------------------------------------------------+-----------+----------+')
        print('| Name                                                  | Installed | Backuped |')
        print('+-------------------------------------------------------+-----------+----------+')

        for it in plugins.PluginsList:
            restricted_characters = '/\\?%*:|"<>'
            file_name = ''.join(filter(lambda x: x not in restricted_characters, it.Name))
            name = it.Name + ('' if it.available else ' (Not available)')
            installed = '+' if it.available and it.detect() else ' '
            backuped = '+' if os.path.exists(os.path.join('.', 'backups', file_name + '.tar.xz')) else ' '

            print('| %-53s |     %s     |    %s     |' % (name, installed, backuped))

        print('+-------------------------------------------------------+-----------+----------+')

    if task == "backup" or task == "restore":
        if not args.all:
            Task = {}
            task_reader = configparser.ConfigParser()
            task_reader.read('task.ini')
            for it in task_reader.sections():
                Task[it] = {}
                for opt in task_reader.options(it):
                    Task[it][opt] = task_reader.getboolean(it, opt)

        for plugin in plugins.PluginsList:
            if args.all or (plugin.Name in Task and Task[plugin.Name][task]):
                if plugin.available:
                    try:
                        print()
                        getattr(plugin, task)()
                    except IOError:
                        pass
                else:
                    print('')
                    print('Game {} isn\'t supported on your current platform...'.format(plugin.Name))
