import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class CrysisPlugin(BasePlugin):
    Name = "Crysis"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Profiles', os.path.join(MyDocumentsPath, 'My Games', 'Crysis'), 'Profiles')
        _.add_folder('Saves', os.path.join(MyDocumentsPath, 'My Games', 'Crysis'), 'SaveGames')
        _.add_files('Config', os.path.join(MyDocumentsPath, 'My Games', 'Crysis'), 'game.cfg')


    def restore(self, _):
        _.restore_folder('Profiles', os.path.join(MyDocumentsPath, 'My Games', 'Crysis'), 'Profiles')
        _.restore_folder('Saves', os.path.join(MyDocumentsPath, 'My Games', 'Crysis'), 'SaveGames')
        _.restore_files('Config', os.path.join(MyDocumentsPath, 'My Games', 'Crysis'), 'game.cfg')


    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'My Games', 'Crysis')):
            return True
        return False
