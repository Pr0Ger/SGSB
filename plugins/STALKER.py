import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamGamesPath


def factory(name, folder):
    class TempPlugin(BasePlugin):
        Name = name
        support_os = ["Windows"]

        def backup(self, _):
            path_to_appdata = os.path.join(SteamGamesPath, folder, '_appdata_')
            _.add_folder('Saves', path_to_appdata, 'savedgames')
            _.add_files('Settings', path_to_appdata, 'user.ltx')

        def restore(self, _):
            path_to_appdata = os.path.join(SteamGamesPath, folder, '_appdata_')
            _.restore_folder('Saves', path_to_appdata, 'savedgames')
            _.restore_files('Settings', path_to_appdata, 'user.ltx')

        def detect(self):
            if os.path.isdir(os.path.join(SteamGamesPath, folder)):
                return True
            return False

    return TempPlugin


STALKERSoCRUPlugin = factory("S.T.A.L.K.E.R.: Shadow of Chernobyl (RU)", 'stalker shadow of chernobyl ru')
STALKERCSPlugin = factory("S.T.A.L.K.E.R.: Clear Sky", 'stalker clear sky')
STALKERCoPPlugin = factory("S.T.A.L.K.E.R.: Call of Pripyat", 'stalker call of pripyat')
