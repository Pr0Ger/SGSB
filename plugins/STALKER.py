import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


class STALKERPlugin(BasePlugin):
    Name = "S.T.A.L.K.E.R."
    support_os = ["Windows"]

    def backup(self):
        super().backup()
        path_to_appdata = os.path.join(SteamGamesPath, 'stalker shadow of chernobyl ru', '_appdata_')
        self.backup_file.add_folder('Saves', path_to_appdata, 'savedgames')
        self.backup_file.add_files('Settings', path_to_appdata, 'user.ltx')

    def restore(self):
        super().restore()
        path_to_appdata = os.path.join(SteamGamesPath, 'stalker shadow of chernobyl ru', '_appdata_')
        self.restore_file.restore_folder('Saves', path_to_appdata, 'savedgames')
        self.restore_files('Settings', path_to_appdata, 'user.ltx')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'stalker shadow of chernobyl ru')):
            return True
        return False
