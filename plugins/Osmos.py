import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class OsmosPlugin(BasePlugin):
    Name = "Osmos"
    support_os = ["Windows", "Darwin"]

    def init(self):
        if self.current_os == 'Windows':
            self.path = MyDocumentsPath

        if self.current_os == 'Darwin':
            self.path = os.path.join('~', 'Library', 'Application Support')
            self.path = os.path.expanduser(self.path)

    def backup(self, _):
        _.add_folder('Profiles', self.path, 'Osmos')

    def restore(self, _):
        _.restore_folder('Profiles', self.path, 'Osmos')

    def detect(self):
        if os.path.isdir(os.path.join(self.path, 'Osmos')):
            return True
        return False
