import os 
from lib.base_plugin import BasePlugin 
from lib.paths import MyDocumentsPath, SteamCloudPath, SteamGamesPath 
  
  
class ShadowWarriorPlugin(BasePlugin): 
    Name = "Shadow Warrior"
    support_os = ["Windows"] 
  
    def backup(self, _): 
        _.add_folder('Saves', MyDocumentsPath, 'Shadow Warrior') 
  
    def restore(self, _): 
        _.restore_folder('Saves', MyDocumentsPath, 'Shadow Warrior') 
  
    def detect(self): 
        if os.path.isdir(os.path.join(MyDocumentsPath, 'Shadow Warrior')): 
            return True
        return False