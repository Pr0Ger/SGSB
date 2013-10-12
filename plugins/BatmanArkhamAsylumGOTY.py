import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class BatmanArkhamAsylumGOTYPlugin(BasePlugin):
    Name = "Batman: Arkham Asylum Game of the Year Edition"
    dependencies = ["Games for Windows Live profile"]
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(MyDocumentsPath, 'Square Enix'), 'Batman Arkham Asylum GOTY')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(MyDocumentsPath, 'Square Enix'), 'Batman Arkham Asylum GOTY')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'Square Enix', 'Batman Arkham Asylum GOTY')):
            return True
        return False
