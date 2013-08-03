import os
from lib.base_plugin import BasePlugin


class TorchlightPlugin(BasePlugin):
    Name = "Torchlight"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(os.environ['APPDATA'], 'runic games', 'torchlight'), 'save')
        _.add_folder('Mods', os.path.join(os.environ['APPDATA'], 'runic games', 'torchlight'), 'mods')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(os.environ['APPDATA'], 'runic games', 'torchlight'), 'save')
        _.restore_folder('Mods', os.path.join(os.environ['APPDATA'], 'runic games', 'torchlight'), 'mods')

    def detect(self):
        if os.path.isdir(os.path.join(os.environ['APPDATA'], 'runic games', 'torchlight')):
            return True
        return False
