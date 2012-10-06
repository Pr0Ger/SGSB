import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class VVVVVVPlugin(BasePlugin):
    Name = "VVVVVV"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(MyDocumentsPath, 'VVVVVV'), 'Saves')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(MyDocumentsPath, 'VVVVVV'), 'Saves')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'VVVVVV', 'Saves')):
            return True
        return False
