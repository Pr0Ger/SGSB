import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath, SteamGamesPath


def factory(name, id, folder):
    class TempPlugin(BasePlugin):
        Name = name
        support_os = ["Windows"]

        def backup(self, _):
            _.add_folder('Data', os.path.join(SteamCloudPath, id), 'remote')

        def restore(self, _):
            _.restore_folder('Data', os.path.join(SteamCloudPath, id), 'remote')

        def detect(self):
            if os.path.isdir(os.path.join(SteamGamesPath, folder)):
                return True
            return False

    return TempPlugin

OrcsMustDie = factory("Orcs Must Die!", '102600', 'orcs must die!')
OrcsMustDie2 = factory("Orcs Must Die! 2", '201790', 'Orcs Must Die 2')
