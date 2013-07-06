import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class FarCry2Plugin(BasePlugin):
    Name = "Far Cry 2"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(MyDocumentsPath, 'My Games'), 'Far Cry 2')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(MyDocumentsPath, 'My Games'), 'Far Cry 2')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'My Games', 'Far Cry 2')):
            return True
        return False
