import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class ApertureTagPlugin(BasePlugin):
    Name = "Aperture Tag: The Paint Gun Testing Initiative"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(SteamGamesPath, 'Aperture Tag', 'aperturetag'), 'save')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(SteamGamesPath, 'Aperture Tag', 'aperturetag'), 'save')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Aperture Tag')):
            return True
        return False
