import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class HitmanCodename47Plugin(BasePlugin):
    Name = "Hitman: Codename 47"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_files('Save', os.path.join(SteamGamesPath, 'Hitman Codename 47'), 'Hitman.sav')

    def restore(self, _):
        _.restore_files('Save', os.path.join(SteamGamesPath, 'Hitman Codename 47'), 'Hitman.sav')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Hitman Codename 47')):
            return True
        return False
