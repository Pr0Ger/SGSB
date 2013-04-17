import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class Hitman2SilentAssassinPlugin(BasePlugin):
    Name = "Hitman 2: Silent Assassin"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(SteamGamesPath, 'Hitman 2 Silent Assassin'), 'Save')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(SteamGamesPath, 'Hitman 2 Silent Assassin'), 'Save')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Hitman 2 Silent Assassin')):
            return True
        return False
