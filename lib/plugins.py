import os
from lib.base_plugin import BasePlugin

plugins_list = {}


def LoadPlugins():
    for File in os.listdir('.' + os.sep + 'plugins'):
        try:
            __import__("plugins." + os.path.splitext(File)[0])
        except ImportError:
            pass

    for it in BasePlugin.__subclasses__():
        tmp = it()
        tmp.init()

        plugins_list[tmp.Name] = tmp
