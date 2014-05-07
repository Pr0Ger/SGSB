import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath, SteamGamesPath


class ZenoClash2Plugin(BasePlugin):
    Name = "Zeno Clash 2"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Data', os.path.join(SteamCloudPath, '215690'), 'remote')

    def restore(self, _):
        _.restore_folder('Data', os.path.join(SteamCloudPath, '215690'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Zeno Clash 2')):
            return True
        return False
