import os
from lib.base_plugin import BasePlugin
from lib.paths import SavedGamesPath

def factory(name, folder):
    class TempPlugin(BasePlugin):
        Name = name
        support_os = ["Windows"]

        def backup(self, _):
            _.add_folder('Saves', os.path.join(SavedGamesPath, 'MachineGames'), folder)

        def restore(self, _):
            _.restore_folder('Saves', os.path.join(SavedGamesPath, 'MachineGames'), folder)

        def detect(self):
            if os.path.isdir(os.path.join(SavedGamesPath, 'MachineGames', folder)):
                return True
            return False
    return TempPlugin

WolfensteinTheNewOrderPlugin = factory("Wolfenstein: The New Order", 'Wolfenstein The New Order')
WolfensteinTheOldBloodPlugin = factory("Wolfenstein: The Old Blood", 'Wolfenstein The Old Blood')