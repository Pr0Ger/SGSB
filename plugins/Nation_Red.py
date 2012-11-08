import os
from lib.base_plugin import BasePlugin


class NationRedPlugin(BasePlugin):
    Name = "Nation Red"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.environ['APPDATA'], 'NationRed')

    def restore(self, _):
        _.restore_folder('Saves', os.environ['APPDATA'], 'NationRed')

    def detect(self):
        if self.current_os == 'Windows':
            if os.path.isdir(os.path.join(os.environ['APPDATA'], 'NationRed')):
                return True
        return False
