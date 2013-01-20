import os
from lib.base_plugin import BasePlugin


class WorldOfGooPlugin(BasePlugin):
    Name = "World of Goo"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(os.environ['LOCALAPPDATA'], '2DBoy'), 'WorldOfGoo')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(os.environ['LOCALAPPDATA'], '2DBoy'), 'WorldOfGoo')

    def detect(self):
        if os.path.isdir(os.path.join(os.environ['LOCALAPPDATA'], '2DBoy', 'WorldOfGoo')):
            return True
        return False
