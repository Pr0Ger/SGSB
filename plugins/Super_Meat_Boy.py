import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class SuperMeatBoyPlugin(BasePlugin):
    Name = "Super Meat Boy"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(SteamGamesPath, 'super meat boy'), 'UserData')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(SteamGamesPath, 'super meat boy'), 'UserData')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'super meat boy')):
            return True
        return False
