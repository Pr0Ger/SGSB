import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class CoD4MWPlugin(BasePlugin):
    Name = "Call of Duty 4: Modern Warfare"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Profiles', os.path.join(SteamGamesPath, 'Call of Duty 4'), 'players')

    def restore(self, _):
        _.restore_folder('Profiles', os.path.join(SteamGamesPath, 'Call of Duty 4'), 'players')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Call of Duty 4')):
            return True
        return False
