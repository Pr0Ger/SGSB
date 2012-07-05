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

    def backup(self):
        super().backup()
        self.backup_file.add_files('Saves', os.path.join(os.environ['APPDATA'], 'Braid'), self.saves)

    def restore(self):
        super().restore()
        self.restore_file.restore_files('Saves', os.path.join(os.environ['APPDATA'], 'Braid'), self.saves)

    def detect(self):
        if self.current_os == 'Windows':
            if os.path.isdir(os.path.join(os.environ['APPDATA'], 'Braid')):
                return True
        return False
