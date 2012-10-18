import os
from lib.base_plugin import BasePlugin
from lib.paths import SavedGamesPath


class YourDoodlesAreBuggedPlugin(BasePlugin):
    Name = "Your Doodles Are Bugged!"
    support_os = ["Windows"]

    def backup(self, _):
        _.add_folder('Saves', SavedGamesPath, 'Your Doodles Are Bugged!')

    def restore(self, _):
        _.restore_folder('Saves', SavedGamesPath, 'Your Doodles Are Bugged!')

    def detect(self):
        if os.path.isdir(os.path.join(SavedGamesPath, 'Your Doodles Are Bugged!')):
            return True
        return False
