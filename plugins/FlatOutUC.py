import os
from lib.base_plugin import BasePlugin


class FlatOutUCPlugin(BasePlugin):
    Name = "FlatOut: Ultimate Carnage"
    dependencies = ["Games for Windows Live profile"]
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Profile', os.environ['LOCALAPPDATA'], 'FlatOut Ultimate Carnage')

    def restore(self, _):
        _.restore_folder('Profile', os.environ['LOCALAPPDATA'], 'FlatOut Ultimate Carnage')

    def detect(self):
        if os.path.isdir(os.path.join(os.environ['LOCALAPPDATA'], 'FlatOut Ultimate Carnage')):
            return True
        return False
