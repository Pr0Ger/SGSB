import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class OsmosPlugin(BasePlugin):
    Name = "Osmos"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Profiles', MyDocumentsPath, 'Osmos')

    def restore(self, _):
        _.restore_folder('Profiles', MyDocumentsPath, 'Osmos')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'Osmos')):
            return True
        return False
