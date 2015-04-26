import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class StarCraftIIPlugin(BasePlugin):
    Name = "StarCraft II"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', MyDocumentsPath, 'StarCraft II')

    def restore(self, _):
        _.restore_folder('Saves', MyDocumentsPath, 'StarCraft II')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'StarCraft II')):
            return True
        return False
