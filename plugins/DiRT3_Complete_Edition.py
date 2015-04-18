import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath, SteamGamesPath


class Dirt3CompletePlugin(BasePlugin):
    Name = "DiRT 3 Complete Edition"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(SteamCloudPath, '321040'), 'remote')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(SteamCloudPath, '321040'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'DiRT 3 Complete Edition')):
            return True
        return False
