import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class FlatOut2Plugin(BasePlugin):
    Name = "FlatOut 2"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(SteamGamesPath, 'FlatOut2'), 'Savegame')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(SteamGamesPath, 'FlatOut2'), 'Savegame')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'FlatOut2')):
            return True
        return False
