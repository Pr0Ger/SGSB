import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath, SteamGamesPath


class TombRaider2013Plugin(BasePlugin):
    Name = "Tomb Raider [2013]"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Data', os.path.join(SteamCloudPath, '203160'), 'remote')

    def restore(self, _):
        _.restore_folder('Data', os.path.join(SteamCloudPath, '203160'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Tomb Raider')):
            return True
        return False
