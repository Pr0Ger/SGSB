import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class VVVVVVPlugin(BasePlugin):
    Name = "VVVVVV"
    support_os = ["Windows", "Darwin"]

    def init(self):
        self.path = os.path.join(MyDocumentsPath, 'VVVVVV')

    def backup(self, _):
        _.add_folder('Saves', self.path, 'Saves')

    def restore(self, _):
        _.restore_folder('Saves', self.path, 'Saves')

    def detect(self):
        if os.path.isdir(os.path.join(self.path, 'Saves')):
            return True
        return False
