import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath, SteamCloudPath, SteamGamesPath


class DiRTShowdownPlugin(BasePlugin):
    Name = "DiRT Showdown"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Config', os.path.join(MyDocumentsPath, 'My Games', 'DiRT Showdown'), 'hardwaresettings')
        _.add_folder('Saves', os.path.join(SteamCloudPath, '201700'), 'remote')

    def restore(self, _):
        _.restore_folder('Config', os.path.join(MyDocumentsPath, 'My Games', 'DiRT Showdown'), 'hardwaresettings')
        _.restore_folder('Saves', os.path.join(SteamCloudPath, '201700'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'DiRT Showdown')):
            return True
        return False
