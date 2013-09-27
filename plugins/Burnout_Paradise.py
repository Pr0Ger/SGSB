import os
from lib.base_plugin import BasePlugin


class BurnoutParadisePlugin(BasePlugin):
    Name = "Burnout Paradise: The Ultimate Box"
    support_os = ["Windows"]
    configs = [
        'config.ini',
        'controls.ini',
        'defaults.ini'
    ]

    def backup(self, _):

        _.add_files('Configs', os.path.join(os.environ['LOCALAPPDATA'], 'Criterion Games', 'Burnout Paradise'), self.configs)
        _.add_folder('Profile', os.path.join(os.environ['LOCALAPPDATA'], 'Criterion Games', 'Burnout Paradise'), 'Save')

    def restore(self, _):
        _.restore_files('Configs', os.path.join(os.environ['LOCALAPPDATA'], 'Criterion Games', 'Burnout Paradise'), self.configs)
        _.restore_folder('Profile', os.path.join(os.environ['LOCALAPPDATA'], 'Criterion Games', 'Burnout Paradise'), 'Save')

    def detect(self):
        if os.path.isdir(os.path.join(os.environ['LOCALAPPDATA'], 'Criterion Games', 'Burnout Paradise')):
            return True
        return False
