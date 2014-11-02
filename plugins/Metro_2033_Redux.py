import os
from lib.base_plugin import BasePlugin
from lib.paths import MyDocumentsPath, SteamGamesPath, SteamCloudPath


class Metro2033ReduxPlugin(BasePlugin):
    Name = "Metro 2033 Redix"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', os.path.join(MyDocumentsPath, '4a games'), 'metro 2033')

    def restore(self, _):
        _.restore_folder('Saves', os.path.join(MyDocumentsPath, '4a games'), 'metro 2033')

    def detect(self):
        if os.path.isdir(os.path.join(SteamGamesPath, 'Metro 2033 Redux')):
            return True
        return False
