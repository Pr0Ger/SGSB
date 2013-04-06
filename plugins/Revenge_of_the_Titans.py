import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath, SteamGamesPath


class RevengeOfTheTitansPlugin(BasePlugin):
    Name = "Revenge of the Titans"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Data', os.path.join(SteamCloudPath, '93200'), 'remote')

    def restore(self, _):
        _.restore_folder('Data', os.path.join(SteamCloudPath, '93200'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Revenge of the Titans')):
            return True
        return False
