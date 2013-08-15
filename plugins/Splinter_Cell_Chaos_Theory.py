import os
from lib.base_plugin import BasePlugin


class SplinterCellChaosTheoryPlugin(BasePlugin):
    Name = "Tom Clancy's Splinter Cell: Chaos Theory"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(os.environ['PROGRAMDATA'], 'Ubisoft'), 'Tom Clancy\'s Splinter Cell Chaos Theory')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(os.environ['PROGRAMDATA'], 'Ubisoft'), 'Tom Clancy\'s Splinter Cell Chaos Theory')

    def detect(self):
        if os.path.isdir(os.path.join(os.environ['PROGRAMDATA'], 'Ubisoft', 'Tom Clancy\'s Splinter Cell Chaos Theory')):
            return True
        return False
