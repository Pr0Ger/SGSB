import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class BorderlandsPlugin(BasePlugin):
    Name = "Borderlands"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(MyDocumentsPath, 'My Games', 'Borderlands'), 'SaveData')
        _.add_folder('Configs', os.path.join(MyDocumentsPath, 'My Games', 'Borderlands', 'WillowGame'), 'Config')


    def restore(self, _):
        _.restore_folder('Saves', os.path.join(MyDocumentsPath, 'My Games', 'Borderlands'), 'SaveData')
        _.restore_folder('Configs', os.path.join(MyDocumentsPath, 'My Games', 'Borderlands', 'WillowGame'), 'Config')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'My Games', 'Borderlands')):
            return True
        return False
