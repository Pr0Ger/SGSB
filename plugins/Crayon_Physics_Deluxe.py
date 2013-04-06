import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class CrayonPhysicsDeluxePlugin(BasePlugin):
    Name = "Crayon Physics Deluxe"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Solutions', MyDocumentsPath, 'Crayon Physics Deluxe')
        _.add_folder('Saves', os.environ['APPDATA'], 'Crayon Physics Deluxe')

    def restore(self, _):
        _.restore_folder('Solutions', MyDocumentsPath, 'Crayon Physics Deluxe')
        _.restore_folder('Saves', os.environ['APPDATA'], 'Crayon Physics Deluxe')

    def detect(self):
        if os.path.isdir(os.path.join(os.environ['APPDATA'], 'Crayon Physics Deluxe')):
            return True
        return False
