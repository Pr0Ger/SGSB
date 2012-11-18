import os
from lib.base_plugin import BasePlugin


class BraidPlugin(BasePlugin):
    Name = "Braid"
    support_os = ["Windows", "Darwin"]
    saves = [
        'slot_0.braid_campaign',
        'slot_1.braid_campaign',
        'slot_2.braid_campaign',
        'slot_3.braid_campaign',
        'slot_4.braid_campaign'
    ]

    def init(self):
        if self.current_os == 'Windows':
            self.path = os.path.join(os.environ['APPDATA'], 'Braid')

        if self.current_os == 'Darwin':
            self.path = os.path.join('~', 'Library', 'Preferences', 'Braid')
            self.path = os.path.expanduser(self.path)

    def backup(self, _):
        _.add_files('Saves', self.path, self.saves)

    def restore(self, _):
        _.restore_files('Saves', self.path, self.saves)

    def detect(self):
        if os.path.isdir(self.path):
            return True

        return False
