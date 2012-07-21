import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class ZombieShooterPlugin(BasePlugin):
    Name = "VVVVVV"
    support_os = ["Windows"]

    def backup(self):
        super().backup()
        self.backup_file.add_folder('Saves', os.path.join(MyDocumentsPath, 'VVVVVV'), 'Saves')

    def restore(self):
        super().restore()
        self.restore_file.restore_folder('Saves', os.path.join(MyDocumentsPath, 'VVVVVV'), 'Saves')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'VVVVVV', 'Saves')):
            return True
        return False
