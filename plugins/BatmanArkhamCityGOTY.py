import os 
from lib.base_plugin import BasePlugin 
from lib.paths import MyDocumentsPath, SteamCloudPath, SteamGamesPath 
  
  
class BatmanArkhamCityGOTYPlugin(BasePlugin): 
    Name = "Batman: Arkham City - Game of the Year Edition"
    support_os = ["Windows"] 
  
    def backup(self, _): 
        _.add_folder('Configs', os.path.join(MyDocumentsPath, 'WB Games', 'Batman Arkham City GOTY', 'BmGame'), 'Config') 
        _.add_folder('Saves', os.path.join(SteamCloudPath, '200260'), 'remote') 
  
    def restore(self, _): 
        _.restore_folder('Configs', os.path.join(MyDocumentsPath, 'WB Games', 'Batman Arkham City GOTY', 'BmGame'), 'Config') 
        _.restore_folder('Saves', os.path.join(SteamCloudPath, '200260'), 'remote') 
  
    def detect(self): 
        if os.path.isdir(os.path.join(SteamGamesPath, 'Batman Arkham City GOTY')): 
            return True
        return False