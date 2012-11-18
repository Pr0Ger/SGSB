import os
from lib.base_plugin import BasePlugin


class FaerieSolitairePlugin(BasePlugin):
    Name = "Faerie Solitaire"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.environ['APPDATA'], 'Faerie Solitaire')

    def restore(self, _):
        _.restore_folder('Saves', os.environ['APPDATA'], 'Faerie Solitaire')

    def detect(self):
        if self.current_os == 'Windows':
            if os.path.isdir(os.path.join(os.environ['APPDATA'], 'Faerie Solitaire')):
                return True
        return False
