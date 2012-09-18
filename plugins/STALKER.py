import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


def factory(name, folder):
    class TempPlugin(BasePlugin):
        Name = name
        support_os = ["Windows"]

        def backup(self):
            super().backup()
            path_to_appdata = os.path.join(SteamGamesPath, folder, '_appdata_')
            self.backup_file.add_folder('Saves', path_to_appdata, 'savedgames')
            self.backup_file.add_files('Settings', path_to_appdata, 'user.ltx')

        def restore(self):
            super().restore()
            path_to_appdata = os.path.join(SteamGamesPath, folder, '_appdata_')
            self.restore_file.restore_folder('Saves', path_to_appdata, 'savedgames')
            self.restore_file.restore_files('Settings', path_to_appdata, 'user.ltx')

        def detect(self):
            if os.path.isdir(os.path.join(SteamGamesPath, folder)):
                return True
            return False

    return TempPlugin


STALKERPlugin = factory("S.T.A.L.K.E.R.: Shadow of Chernobyl (RU)", 'stalker shadow of chernobyl ru')
STALKERPlugin = factory("S.T.A.L.K.E.R.: Clear Sky", 'stalker clear sky')
STALKERPlugin = factory("S.T.A.L.K.E.R.: Call of Pripyat", 'stalker call of pripyat')
