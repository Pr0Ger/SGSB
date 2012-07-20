import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class ZombieShooterPlugin(BasePlugin):
    Name = "Zombie Shooter 2"
    support_os = ["Windows"]

    def backup(self):
        super().backup()
        self.backup_file.add_folder('Saves', MyDocumentsPath, 'Zombie Shooter 2 Saves')

    def restore(self):
        super().restore()
        self.restore_file.restore_folder('Saves', MyDocumentsPath, 'Zombie Shooter 2 Saves')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'Zombie Shooter 2 Saves')):
            return True
        return False
