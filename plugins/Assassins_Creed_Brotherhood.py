import os
from lib.base_plugin import BasePlugin
from lib.paths import SavedGamesPath


class AssassinsCreedBrotherhoodPlugin(BasePlugin):
    Name = "Assassin's Creed Brotherhood"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', SavedGamesPath, 'Assassin\'s Creed Brotherhood')

    def restore(self, _):
        _.restore_folder('Saves', SavedGamesPath, 'Assassin\'s Creed Brotherhood')

    def detect(self):
        if os.path.isdir(os.path.join(SavedGamesPath, 'Assassin\'s Creed Brotherhood')):
            return True
        return False
