import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath, SteamCloudPath, SteamGamesPath


class LifeIsStrangePlugin(BasePlugin):
    Name = "Life Is Strange"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_files('Profile', os.path.join(SteamCloudPath, '319630', 'remote'), 'profile.bin')
        _.add_folder('Saves', os.path.join(MyDocumentsPath, 'My Games'), 'Life Is Strange')

    def restore(self, _):
        _.restore_files('Profile', os.path.join(SteamCloudPath, '319630', 'remote'), 'profile.bin')
        _.restore_folder('Saves', os.path.join(MyDocumentsPath, 'My Games'), 'Life Is Strange')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Life Is Strange')):
            return True
        return False
