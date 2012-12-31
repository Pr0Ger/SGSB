import os
from lib.base_plugin import BasePlugin


class GFWLPlugin(BasePlugin):
    Name = "Games for Windows Live profile"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Profile', os.path.join(os.environ['LOCALAPPDATA'], 'Microsoft'), 'XLive')

    def restore(self, _):
        _.restore_folder('Profile', os.path.join(os.environ['LOCALAPPDATA'], 'Microsoft'), 'XLive')

    def detect(self):
        if os.path.isdir(os.path.join(os.environ['LOCALAPPDATA'], 'Microsoft', 'XLive')):
            return True
        return False
