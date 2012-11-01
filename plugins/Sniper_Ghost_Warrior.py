import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class SniperGhostWarriorPlugin(BasePlugin):
    Name = "Sniper: Ghost Warrior"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Profiles', os.path.join(MyDocumentsPath, 'Sniper - Ghost Warrior', 'out'), 'profiles')
        _.add_folder('Saves', os.path.join(MyDocumentsPath, 'Sniper - Ghost Warrior', 'out'), 'save')
        _.add_folder('Settings', os.path.join(MyDocumentsPath, 'Sniper - Ghost Warrior', 'out'), 'Settings')
        _.add_files('Other', os.path.join(MyDocumentsPath, 'Sniper - Ghost Warrior', 'out'), ['FirstRun.scr', 'LastUser.scr', 'save.tga'])

    def restore(self, _):
        _.restore_folder('Profiles', os.path.join(MyDocumentsPath, 'Sniper - Ghost Warrior', 'out'), 'profiles')
        _.restore_folder('Saves', os.path.join(MyDocumentsPath, 'Sniper - Ghost Warrior', 'out'), 'save')
        _.restore_folder('Settings', os.path.join(MyDocumentsPath, 'Sniper - Ghost Warrior', 'out'), 'Settings')
        _.restore_files('Other', os.path.join(MyDocumentsPath, 'Sniper - Ghost Warrior', 'out'), ['FirstRun.scr', 'LastUser.scr', 'save.tga'])

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'Sniper - Ghost Warrior')):
            return True
        return False
