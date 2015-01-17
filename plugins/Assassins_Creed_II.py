import os
from lib.base_plugin import BasePlugin
from lib.path import UbisoftSaves


class AssassinsCreedIIPlugin(BasePlugin):
    Name = "Assassin's Creed II"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Settings', os.path.join(os.environ['APPDATA'], 'Ubisoft'), 'Assassin\'s Creed 2')
        _.add_folder('Saves', UbisoftSaves, '4')

    def restore(self, _):
        _.restore_folder('Settings', os.path.join(os.environ['APPDATA'], 'Ubisoft'), 'Assassin\'s Creed 2')
        _.restore_folder('Saves', UbisoftSaves, '4')

    def detect(self):
        if os.path.isdir(os.path.join(os.environ['APPDATA'], 'Ubisoft', 'Assassin\'s Creed 2')):
            return True
        return False
