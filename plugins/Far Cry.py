import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class FarCryPlugin(BasePlugin):
    Name = "Far Cry"
    support_os = ["Windows"]

    def backup(self):
        super().backup()
        self.backup_file.add_folder('Profiles', os.path.join(SteamGamesPath, 'farcry'), 'Profiles')

    def restore(self):
        super().restore()
        self.restore_file.restore_folder('Profiles', os.path.join(SteamGamesPath, 'farcry'), 'Profiles')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'farcry')):
            return True
        return False
