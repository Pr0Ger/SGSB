import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath, SteamGamesPath


class OrcsMustDiePlugin(BasePlugin):
    Name = "Orcs Must Die!"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Data', os.path.join(SteamCloudPath, '102600'), 'remote')

    def restore(self, _):
        _.restore_folder('Data', os.path.join(SteamCloudPath, '102600'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'orcs must die!')):
            return True
        return False
