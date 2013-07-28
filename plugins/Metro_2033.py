import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath, SteamGamesPath, SteamCloudPath


class Metro2033Plugin(BasePlugin):
    Name = "Metro 2033"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(MyDocumentsPath, '4a games'), 'metro 2033')
        _.add_files('Config', os.path.join(SteamCloudPath, '43110', 'remote'), 'user.cfg')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(MyDocumentsPath, '4a games'), 'metro 2033')
        _.restore_files('Config', os.path.join(SteamCloudPath, '43110', 'remote'), 'user.cfg')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'metro 2033')):
            return True
        return False
