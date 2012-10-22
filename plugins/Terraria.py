import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class TerrariaPlugin(BasePlugin):
    Name = "Terraria"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Profiles', os.path.join(MyDocumentsPath, 'My Games', 'Terraria'), 'Players')
        _.add_folder('Worlds', os.path.join(MyDocumentsPath, 'My Games', 'Terraria'), 'Worlds')
        _.add_files('Config', os.path.join(MyDocumentsPath, 'My Games', 'Terraria'), ['config.dat', 'servers.dat'])


    def restore(self, _):
        _.restore_folder('Profiles', os.path.join(MyDocumentsPath, 'My Games', 'Terraria'), 'Players')
        _.restore_folder('Worlds', os.path.join(MyDocumentsPath, 'My Games', 'Terraria'), 'Worlds')
        _.restore_files('Config', os.path.join(MyDocumentsPath, 'My Games', 'Terraria'), ['config.dat', 'servers.dat'])

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'My Games', 'Terraria')):
            return True
        return False
