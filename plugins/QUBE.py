import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class QUBEPlugin(BasePlugin):
    Name = "Q.U.B.E."
    support_os = ["Windows"]

    def backup(self, _):
        _.add_files('Save', os.path.join(SteamGamesPath, 'qube', 'UDKGame', 'Config'), 'UDKGame.ini')

    def restore(self, _):
        _.restore_files('Save', os.path.join(SteamGamesPath, 'qube', 'UDKGame', 'Config'), 'UDKGame.ini')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'qube')):
            return True
        return False
