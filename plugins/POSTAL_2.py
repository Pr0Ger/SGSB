import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class POSTAL2Plugin(BasePlugin):
    Name = "POSTAL 2"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(SteamGamesPath, 'POSTAL2Complete'), 'Save')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(SteamGamesPath, 'POSTAL2Complete'), 'Save')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'POSTAL2Complete')):
            return True
        return False
