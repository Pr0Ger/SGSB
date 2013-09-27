import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class SleepingDogsPlugin(BasePlugin):
    Name = "Sleeping Dogs"
    support_os = ["Windows"]
    saves = [
        'DisplaySettings.xml',
        'HK Autosave Slot',
        'HK GameSlot 1',
        'HK GameSlot 2',
        'HK GameSlot 3',
        'HK GameSlot 4',
        'HK AutosaveG Slot',
        'HK GameSlotG 1',
        'HK GameSlotG 2',
        'HK AutosaveN Slot',
        'HK GameSlotN 1',
        'HK GameSlotN 2',
        'HK Options'
    ]

    def backup(self, _):
        _.add_files('Saves', os.path.join(SteamGamesPath, 'SleepingDogs', 'Data'), self.saves)

    def restore(self, _):
        _.restore_files('Saves', os.path.join(SteamGamesPath, 'SleepingDogs', 'Data'), self.saves)

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'SleepingDogs')):
            return True
        return False
