import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath, SteamGamesPath


class BatmanArkhamAsylumGOTYPlugin(BasePlugin):
    Name = "Batman: Arkham Asylum Game of the Year Edition"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(SteamCloudPath, '35140'), 'remote')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(SteamCloudPath, '35140'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Batman Arkham Asylum GOTY')):
            return True
        return False
