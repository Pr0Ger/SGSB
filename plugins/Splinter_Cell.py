import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class SplinterCellPlugin(BasePlugin):
    Name = "Tom Clancy's Splinter Cell"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(SteamGamesPath, 'Splinter Cell'), 'Save')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(SteamGamesPath, 'Splinter Cell'), 'Save')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Splinter Cell')):
            return True
        return False
