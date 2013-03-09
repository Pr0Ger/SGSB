import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class TheBindingOfIsaacPlugin(BasePlugin):
    Name = "The Binding of Isaac"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_files('Save', os.path.join(SteamGamesPath, 'the binding of isaac'), ['myFile.txt', 'serial.txt'])

    def restore(self, _):
        _.restore_files('Save', os.path.join(SteamGamesPath, 'the binding of isaac'), ['myFile.txt', 'serial.txt'])

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'the binding of isaac')):
            return True
        return False
