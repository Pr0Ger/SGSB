import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath, SteamGamesPath


class PlantsVsZombiesPlugin(BasePlugin):
    Name = "Plants vs. Zombies"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Data', os.path.join(SteamCloudPath, '3590'), 'remote')

    def restore(self, _):
        _.restore_folder('Data', os.path.join(SteamCloudPath, '3590'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'plants vs zombies')):
            return True
        return False
