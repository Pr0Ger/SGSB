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

        for name in sorted(plugins.plugins_list):
            it = plugins.plugins_list[name]
            restricted_characters = '/\\?%*:|"<>'
            file_name = ''.join(filter(lambda x: x not in restricted_characters, it.Name))
            name = it.Name + ('' if it.available else ' (Not available)')
            installed = '+' if it.available and it.detect() else ' '
            backuped = '+' if os.path.exists(os.path.join('.', 'backups', file_name + '.tar.xz')) else ' '

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
                            print("WARN: Plugin '{}' require broken '{}' plugin.")
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
