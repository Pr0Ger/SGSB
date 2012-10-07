import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class PokerNightPlugin(BasePlugin):
    Name = "Poker Night at the Inventory"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(MyDocumentsPath, 'Telltale Games'), 'Poker Night at the Inventory')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(MyDocumentsPath, 'Telltale Games'), 'Poker Night at the Inventory')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'Telltale Games', 'Poker Night at the Inventory')):
            return True
        return False
