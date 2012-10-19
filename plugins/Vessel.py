import os
from lib.base_plugin import BasePlugin


class VesselPlugin(BasePlugin):
    Name = "Vessel"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.environ['APPDATA'], 'Vessel')

    def restore(self, _):
        _.restore_folder('Saves', os.environ['APPDATA'], 'Vessel')

    def detect(self):
        if self.current_os == 'Windows':
            if os.path.isdir(os.path.join(os.environ['APPDATA'], 'Vessel')):
                return True
        return False
