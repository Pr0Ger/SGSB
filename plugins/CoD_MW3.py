import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class CoDMW3Plugin(BasePlugin):
    Name = "Call of Duty: Modern Warfare 3"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Profiles', os.path.join(SteamGamesPath, 'call of duty modern warfare 3'), 'players2')

    def restore(self, _):
        _.restore_folder('Profiles', os.path.join(SteamGamesPath, 'call of duty modern warfare 3'), 'players2')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'call of duty modern warfare 3')):
            return True
        return False
