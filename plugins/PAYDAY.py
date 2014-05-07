import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath, SteamGamesPath


class PAYDAYPlugin(BasePlugin):
    Name = "PAYDAY: The Heist"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Data', os.path.join(SteamCloudPath, '24240'), 'remote')

    def restore(self, _):
        _.restore_folder('Data', os.path.join(SteamCloudPath, '24240'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'payday the heist')):
            return True
        return False
