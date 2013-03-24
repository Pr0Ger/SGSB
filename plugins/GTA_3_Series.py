import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


def factory(name, folder):
    class TempPlugin(BasePlugin):
        Name = name
        support_os = ["Windows"]

        def backup(self, _):
            _.add_folder('Saves', MyDocumentsPath, folder)

        def restore(self, _):
            _.restore_folder('Saves', MyDocumentsPath, folder)

        def detect(self):
            if os.path.isdir(os.path.join(MyDocumentsPath, folder)):
                return True
            return False

    return TempPlugin

GTA3Plugin = factory("Grand Theft Auto III", 'GTA3 User Files')
GTAViceCityPlugin = factory("Grand Theft Auto: Vice City", 'GTA Vice City User Files')
GTASanAndreasPlugin = factory("Grand Theft Auto: San Andreas", 'GTA San Andreas User Files')
