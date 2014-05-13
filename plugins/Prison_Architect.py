import os
from lib.base_plugin import BasePlugin


class PrisonArchitectPlugin(BasePlugin):
    Name = "Prison Architect"
    support_os = ["Windows", "Darwin"]

    def init(self):
        if self.current_os == 'Windows':
            self.path = os.path.join(os.environ['LOCALAPPDATA'], 'Introversion')

        if self.current_os == 'Darwin':
            self.path = os.path.join('~', 'Library', 'Application Support')
            self.path = os.path.expanduser(self.path)

    def backup(self, _):
        _.add_folder('Data', self.path, 'Prison Architect')

    def restore(self, _):
        _.restore_folder('Data', self.path, 'Prison Architect')

    def detect(self):
        if os.path.isdir(os.path.join(self.path, 'Prison Architect')):
            return True
        return False
