import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


def factory(name, folder):
    class TempPlugin(BasePlugin):
        Name = name
        support_os = ["Windows"]

        def backup(self, _):
            _.add_folder('Saves', os.path.join(SteamGamesPath, folder, 'hl2'), 'save')

        def restore(self, _):
            _.restore_folder('Saves', os.path.join(SteamGamesPath, folder, 'hl2'), 'save')

        def detect(self):
            if os.path.isdir(os.path.join(SteamGamesPath, folder)):
                return True
            return False

    return TempPlugin


HL2Plugin = factory("Half-Life 2", 'Half-Life 2')
HL2UpdatePlugin = factory("Half-Life 2: Update", 'Half-Life 2 Update')
