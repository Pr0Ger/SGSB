import os
from lib.base_plugin import BasePlugin
from lib.paths import UbisoftSaves


class AssassinsCreedRevelationsPlugin(BasePlugin):
    Name = "Assassin's Creed Revelations"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Settings', MyDocumentsPath, 'Assassin\'s Creed Revelations')
        _.add_folder('Saves', UbisoftSaves, '40')

    def restore(self, _):
        _.restore_folder('Settings', MyDocumentsPath, 'Assassin\'s Creed Revelations')
        _.restore_folder('Saves', UbisoftSaves, '40')

    def detect(self):
        if os.path.isdir(MyDocumentsPath, 'Assassin\'s Creed Revelations'):
            return True
        return False
