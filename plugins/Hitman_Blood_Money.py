import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class HitmanBloodMoneyPlugin(BasePlugin):
    Name = "Hitman: Blood Money"
    support_os = ["Windows"]

    def backup(self):
        super().backup()
        self.backup_file.add_folder('Profiles', os.path.join(MyDocumentsPath, 'Hitman Blood Money'), 'Profiles')

    def restore(self):
        super().restore()
        self.restore_file.restore_folder('Profiles', os.path.join(MyDocumentsPath, 'Hitman Blood Money'), 'Profiles')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'Hitman Blood Money', 'Profiles')):
            return True
        return False
