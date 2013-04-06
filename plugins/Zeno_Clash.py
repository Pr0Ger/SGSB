import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath, SteamGamesPath


class ZenoClashPlugin(BasePlugin):
    Name = "Zeno Clash"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(SteamGamesPath, 'zenoclash', 'zenozoik'), 'SAVE')
        _.add_files('Config', os.path.join(SteamCloudPath, '22200', 'remote', 'cfg'), 'config.cfg')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(SteamGamesPath, 'zenoclash', 'zenozoik'), 'SAVE')
        _.restore_files('Config', os.path.join(SteamCloudPath, '22200', 'remote', 'cfg'), 'config.cfg')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'zenoclash')):
            return True
        return False
