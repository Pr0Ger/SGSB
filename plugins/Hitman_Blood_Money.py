import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class HitmanBloodMoneyPlugin(BasePlugin):
    Name = "Hitman: Blood Money"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Profiles', os.path.join(MyDocumentsPath, 'Hitman Blood Money'), 'Profiles')

    def restore(self, _):
        _.restore_folder('Profiles', os.path.join(MyDocumentsPath, 'Hitman Blood Money'), 'Profiles')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'Hitman Blood Money', 'Profiles')):
            return True
        return False
