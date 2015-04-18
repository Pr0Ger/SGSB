import os
from lib.base_plugin import BasePlugin
from lib.paths import SteamCloudPath


class DeusExHumanRevolutionPlugin(BasePlugin):
    Name = "Deus Ex: Human Revolution"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Settings', os.environ['LOCALAPPDATA'], 'dxhr')
        _.add_folder('Saves_DirectorsCut', os.path.join(SteamCloudPath, '238010'), 'remote')

    def restore(self, _):
        _.restore_folder('Settings', os.environ['LOCALAPPDATA'], 'dxhr')
        _.restore_folder('Saves_DirectorsCut', os.path.join(SteamCloudPath, '238010'), 'remote')

    def detect(self):
        if os.path.isdir(os.path.join(os.environ['LOCALAPPDATA'], 'dxhr')):
            return True
        return False
