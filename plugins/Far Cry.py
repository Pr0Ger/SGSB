import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class FarCryPlugin(BasePlugin):
    Name = "Far Cry"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Profiles', os.path.join(SteamGamesPath, 'farcry'), 'Profiles')

    def restore(self, _):
        _.restore_folder('Profiles', os.path.join(SteamGamesPath, 'farcry'), 'Profiles')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'farcry')):
            return True
        return False
