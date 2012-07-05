import os
from lib.base_plugin import BasePlugin

PluginsList = []


def LoadPlugins():
    for File in os.listdir('.' + os.sep + 'plugins'):
        try:
            __import__("plugins." + os.path.splitext(File)[0])
        except ImportError:
            pass

    for it in BasePlugin.__subclasses__():
        PluginsList.append(it())
