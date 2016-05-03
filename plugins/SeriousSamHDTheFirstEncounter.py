import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath, SteamGamesPath


class SeriousSamHDFirstEncounterPlugin(BasePlugin):
    Name = "Serious Sam HD: The First Encounter"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Data', os.path.join(SteamCloudPath, '41000'), 'remote')

    def restore(self, _):
        _.restore_folder('Data', os.path.join(SteamCloudPath, '41000'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Serious Sam HD The First Encounter')):
            return True
        return False
