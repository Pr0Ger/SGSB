import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath, SteamGamesPath


class WormsReloadedPlugin(BasePlugin):
    Name = "Worms Reloaded"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Data', os.path.join(SteamCloudPath, '22600'), 'remote')

    def restore(self, _):
        _.restore_folder('Data', os.path.join(SteamCloudPath, '22600'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'worms reloaded')):
            return True
        return False
