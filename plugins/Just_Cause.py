import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath


class JustCausePlugin(BasePlugin):
    Name = "Just Cause"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', MyDocumentsPath, 'JustCause')

    def restore(self, _):
        _.restore_folder('Saves', MyDocumentsPath, 'JustCause')

    def detect(self):
        if os.path.isdir(os.path.join(MyDocumentsPath, 'JustCause')):
            return True
        return False
