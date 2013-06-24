import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath, SteamCloudPath, SteamGamesPath


class AlanWakesAmericanNightmarePlugin(BasePlugin):
    Name = "Alan Wake's American Nightmare"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Settings', os.path.join(MyDocumentsPath, 'Remedy'), 'AmericanNightmare')
        _.add_folder('Saves', os.path.join(SteamCloudPath, '202750'), 'remote')

    def restore(self, _):
        _.restore_folder('Settings', os.path.join(MyDocumentsPath, 'Remedy'), 'AmericanNightmare')
        _.add_folder('Saves', os.path.join(SteamCloudPath, '202750'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'alan wakes american nightmare')):
            return True
        return False
