import os 
from lib.base_plugin import BasePlugin 
from lib.paths import MyDocumentsPath, SteamCloudPath, SteamGamesPath 
  
  
class BatmanArkhamOriginsPlugin(BasePlugin): 
    Name = "Batman: Arkham Origins"
    support_os = ["Windows"] 
  
    def backup(self, _): 
        _.add_folder('Configs', os.path.join(MyDocumentsPath, 'WB Games'), 'Batman Arkham Origins') 
        _.add_folder('Saves', os.path.join(SteamCloudPath, '209000'), 'remote') 
  
    def restore(self, _): 
        _.restore_folder('Configs', os.path.join(MyDocumentsPath, 'WB Games'), 'Batman Arkham Origins') 
        _.restore_folder('Saves', os.path.join(SteamCloudPath, '209000'), 'remote') 
  
    def detect(self): 
        if os.path.isdir(os.path.join(SteamGamesPath, 'Batman Arkham Origins')): 
            return True
        return False