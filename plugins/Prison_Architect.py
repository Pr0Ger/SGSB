import os
from lib.base_plugin import BasePlugin


class PrisonArchitectPlugin(BasePlugin):
    Name = "Prison Architect"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Data', os.path.join(os.environ['LOCALAPPDATA'], 'Introversion'), 'Prison Architect')

    def restore(self, _):
        _.restore_folder('Data', os.path.join(os.environ['LOCALAPPDATA'], 'Introversion'), 'Prison Architect')

    def detect(self):
        if os.path.isdir(os.path.join(os.environ['LOCALAPPDATA'], 'Introversion', 'Prison Architect')):
            return True
        return False
