import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath, SteamCloudPath, SteamGamesPath


class SniperEliteV2Plugin(BasePlugin):
    Name = "Sniper Elite V2"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Profile', os.environ['LOCALAPPDATA'], 'SniperV2')
        _.add_folder('Saves', os.path.join(SteamCloudPath, '63380'), 'remote')

    def restore(self, _):
        _.restore_folder('Settings', os.environ['LOCALAPPDATA'], 'SniperV2')
        _.restore_folder('Saves', os.path.join(SteamCloudPath, '63380'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Sniper Elite V2')):
            return True
        return False
