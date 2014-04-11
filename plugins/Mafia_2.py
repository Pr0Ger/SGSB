import os
from lib.base_plugin import BasePlugin


class Mafia2Plugin(BasePlugin):
    Name = "Mafia II"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(os.environ['LOCALAPPDATA'], '2K Games'), 'Mafia II')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(os.environ['LOCALAPPDATA'], '2K Games'), 'Mafia II')

    def detect(self):
        if os.path.isdir(os.path.join(os.environ['LOCALAPPDATA'], '2K Games', 'Mafia II')):
            return True
        return False
