import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class LANoirePlugin(BasePlugin):
    Name = "L.A. Noire"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(MyDocumentsPath, 'Rockstar Games'), 'L.A. Noire')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(MyDocumentsPath, 'Rockstar Games'), 'L.A. Noire')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'Rockstar Games', 'L.A. Noire')):
            return True
        return False
