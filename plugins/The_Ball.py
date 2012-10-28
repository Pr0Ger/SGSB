import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class TheBallPlugin(BasePlugin):
    Name = "The Ball"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(MyDocumentsPath, 'My Games', 'The Ball', 'UDKGame'), 'Config')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(MyDocumentsPath, 'My Games', 'The Ball', 'UDKGame'), 'Config')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'My Games', 'The Ball')):
            return True
        return False
