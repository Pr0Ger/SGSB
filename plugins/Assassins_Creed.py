import os
from lib.base_plugin import BasePlugin


class AssassinsCreedPlugin(BasePlugin):
    Name = "Assassin's Creed"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(os.environ['APPDATA'], 'Ubisoft'), 'Assassin\'s Creed')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(os.environ['APPDATA'], 'Ubisoft'), 'Assassin\'s Creed')

    def detect(self):
        if os.path.isdir(os.path.join(os.environ['APPDATA'], 'Ubisoft', 'Assassin\'s Creed')):
            return True
        return False
