import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath, SteamGamesPath


class LIMBOPlugin(BasePlugin):
    Name = "LIMBO"
    support_os = ["Windows", "Darwin"]

    def backup(self, _):
        _.add_folder('Data', os.path.join(SteamCloudPath, '48000'), 'remote')

    def restore(self, _):
        _.restore_folder('Data', os.path.join(SteamCloudPath, '48000'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'limbo')):
            return True
        return False
