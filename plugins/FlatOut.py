import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class FlatOutPlugin(BasePlugin):
    Name = "FlatOut"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(SteamGamesPath, 'FlatOut'), 'Savegame')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(SteamGamesPath, 'FlatOut'), 'Savegame')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'FlatOut')):
            return True
        return False
