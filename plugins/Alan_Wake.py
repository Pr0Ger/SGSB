import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath, SteamCloudPath, SteamGamesPath


class AlanWakePlugin(BasePlugin):
    Name = "Alan Wake"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Settings', os.path.join(MyDocumentsPath, 'Remedy'), 'AlanWake')
        _.add_folder('Saves', os.path.join(SteamCloudPath, '108710'), 'remote')

    def restore(self, _):
        _.restore_folder('Settings', os.path.join(MyDocumentsPath, 'Remedy'), 'AlanWake')
        _.add_folder('Saves', os.path.join(SteamCloudPath, '108710'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Alan Wake')):
            return True
        return False
