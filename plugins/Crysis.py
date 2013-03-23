import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


def factory(name, folder):
    class TempPlugin(BasePlugin):
        Name = name
        support_os = ["Windows"]

        def backup(self, _):
            _.add_folder('Profiles', os.path.join(MyDocumentsPath, 'My Games', folder), 'Profiles')
            _.add_folder('Saves', os.path.join(MyDocumentsPath, 'My Games', folder), 'SaveGames')
            _.add_files('Config', os.path.join(MyDocumentsPath, 'My Games', folder), 'game.cfg')

        def restore(self, _):
            _.restore_folder('Profiles', os.path.join(MyDocumentsPath, 'My Games', folder), 'Profiles')
            _.restore_folder('Saves', os.path.join(MyDocumentsPath, 'My Games', folder), 'SaveGames')
            _.restore_files('Config', os.path.join(MyDocumentsPath, 'My Games', folder), 'game.cfg')

        def detect(self):
            if os.path.isdir(os.path.join(MyDocumentsPath, 'My Games', folder)):
                return True
            return False

    return TempPlugin

CrysisPlugin = factory("Crysis", 'Crysis')
CrysisWarheadPlugin = factory("Crysis Warhead", 'Crysis_WARHEAD')
