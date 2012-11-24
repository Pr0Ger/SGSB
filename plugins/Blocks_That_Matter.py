import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class BlocksThatMatterPlugin(BasePlugin):
    Name = "Blocks That Matter"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(SteamGamesPath, 'Blocks That Matter'), 'Blocks That Matter Save')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(SteamGamesPath, 'Blocks That Matter'), 'Blocks That Matter Save')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Blocks That Matter')):
            return True
        return False
