import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class ZombieShooter2Plugin(BasePlugin):
    Name = "Zombie Shooter 2"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', MyDocumentsPath, 'Zombie Shooter 2 Saves')

    def restore(self, _):
        _.restore_folder('Saves', MyDocumentsPath, 'Zombie Shooter 2 Saves')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'Zombie Shooter 2 Saves')):
            return True
        return False
