import os
from lib.base_plugin import BasePlugin


class ZombieDriverPlugin(BasePlugin):
    Name = "Zombie Driver"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_files('Settings', os.path.join(os.environ['APPDATA'], 'ZombieDriver'), [
            'controller.cfg',
            'Ogre17.cfg',
            'ZombieDriver.cfg',
        ])
        _.add_folder('Saves', os.path.join(os.environ['APPDATA'], 'ZombieDriver'), 'Save')

    def restore(self, _):
        _.restore_files('Saves', os.path.join(os.environ['APPDATA'], 'ZombieDriver'), [
            'controller.cfg',
            'Ogre17.cfg',
            'ZombieDriver.cfg',
        ])
        _.restore_folder('Saves', os.path.join(os.environ['APPDATA'], 'ZombieDriver'), 'Save')

    def detect(self):
        if os.path.isdir(os.path.join(os.environ['APPDATA'], 'ZombieDriver')):
            return True
        return False
