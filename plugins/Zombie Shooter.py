import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class ZombieShooterPlugin(BasePlugin):
    Name = "Zombie Shooter"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', MyDocumentsPath, 'ZombieShooter Saves')

    def restore(self, _):
        _.restore_folder('Saves', MyDocumentsPath, 'ZombieShooter Saves')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'ZombieShooter Saves')):
            return True
        return False
