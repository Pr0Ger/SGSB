import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath, SavedGamesPath


def factory(name, folder):
    class TempPlugin(BasePlugin):
        Name = name
        support_os = ["Windows"]

        def backup(self, _):
            _.add_folder('Profiles', folder, 'Profiles')
            _.add_folder('Saves', folder, 'SaveGames')
            _.add_files('Config', folder, 'game.cfg')

        def restore(self, _):
            _.restore_folder('Profiles', folder, 'Profiles')
            _.restore_folder('Saves', folder, 'SaveGames')
            _.restore_files('Config', folder, 'game.cfg')

        def detect(self):
            if os.path.isdir(folder):
                return True
            return False

    return TempPlugin

CrysisPlugin = factory("Crysis", os.path.join(MyDocumentsPath, 'My Games', 'Crysis'))
CrysisWarheadPlugin = factory("Crysis Warhead", os.path.join(MyDocumentsPath, 'My Games', 'Crysis_WARHEAD'))
Crysic2Plugin = factory("Crysis 2", os.path.join(SavedGamesPath, 'Crysis2'))
