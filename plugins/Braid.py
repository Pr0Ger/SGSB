import os
from lib.base_plugin import BasePlugin


class BraidPlugin(BasePlugin):
    Name = "Braid"
    support_os = ["Windows"]
    saves = [
        'slot_0.braid_campaign',
        'slot_1.braid_campaign',
        'slot_2.braid_campaign',
        'slot_3.braid_campaign',
        'slot_4.braid_campaign'
    ]

    def backup(self, _):
        _.add_files('Saves', os.path.join(os.environ['APPDATA'], 'Braid'), self.saves)

    def restore(self, _):
        _.restore_files('Saves', os.path.join(os.environ['APPDATA'], 'Braid'), self.saves)

    def detect(self):
        if self.current_os == 'Windows':
            if os.path.isdir(os.path.join(os.environ['APPDATA'], 'Braid')):
                return True
        return False
