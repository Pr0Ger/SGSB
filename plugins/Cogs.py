import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath, SteamGamesPath


class CogsPlugin(BasePlugin):
    Name = "Cogs"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Data', os.path.join(SteamCloudPath, '26500'), 'remote')

    def restore(self, _):
        _.restore_folder('Data', os.path.join(SteamCloudPath, '26500'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'cogs')):
            return True
        return False
