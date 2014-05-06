import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class CoDBOPlugin(BasePlugin):
    Name = "Call of Duty: Black Ops"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Profiles', os.path.join(SteamGamesPath, 'call of duty black ops'), 'players')

    def restore(self, _):
        _.restore_folder('Profiles', os.path.join(SteamGamesPath, 'call of duty black ops'), 'players')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'call of duty black ops')):
            return True
        return False
