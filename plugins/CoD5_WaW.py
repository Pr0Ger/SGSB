import os
from lib.base_plugin import BasePlugin


class CoDWaWPlugin(BasePlugin):
    Name = "Call of Duty: World at War"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Profile', os.path.join(os.environ['LOCALAPPDATA'], 'Activision'), 'CoDWaW')

    def restore(self, _):
        _.restore_folder('Profile', os.path.join(os.environ['LOCALAPPDATA'], 'Activision'), 'CoDWaW')

    def detect(self):
        if os.path.isdir(os.path.join(os.environ['LOCALAPPDATA'], 'Activision', 'CoDWaW')):
            return True
        return False
