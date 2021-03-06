import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class Dirt2Plugin(BasePlugin):
    Name = "Colin McRae DiRT 2"
    dependencies = ["Games for Windows Live profile"]
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(MyDocumentsPath, 'My Games'), 'DiRT2')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(MyDocumentsPath, 'My Games'), 'DiRT2')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'My Games', 'DiRT2')):
            return True
        return False
