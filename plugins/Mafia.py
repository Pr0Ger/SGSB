import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class MafiaPlugin(BasePlugin):
    Name = "Mafia: The City of Lost Heaven"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(SteamGamesPath, 'mafia'), 'savegame')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(SteamGamesPath, 'mafia'), 'savegame')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'mafia')):
            return True
        return False
