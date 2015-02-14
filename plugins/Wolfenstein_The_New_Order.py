import os
from lib.base_plugin import BasePlugin
from lib.paths import SavedGamesPath


class WolfensteinTheNewOrderPlugin(BasePlugin):
    Name = "Wolfenstein: The New Order"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(SavedGamesPath, 'MachineGames'), 'Wolfenstein The New Order')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(SavedGamesPath, 'MachineGames'), 'Wolfenstein The New Order')

    def detect(self):
        if os.path.isdir(os.path.join(SavedGamesPath, 'MachineGames', 'Wolfenstein The New Order')):
            return True
        return False
