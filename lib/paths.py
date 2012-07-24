import os
import platform


MyDocumentsPath = None
SteamGamesPath = None

if platform.system() == 'Windows':
    import ctypes
    from ctypes.wintypes import MAX_PATH

    dll = ctypes.windll.shell32
    buf = ctypes.create_unicode_buffer(MAX_PATH + 1)
    if dll.SHGetSpecialFolderPathW(None, buf, 0x0005, False):
        MyDocumentsPath = buf.value

    from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx

    try:
        key = OpenKey(HKEY_CURRENT_USER, 'Software\\Valve\\Steam')
        SteamPath = QueryValueEx(key, 'SteamPath')[0]
        SteamGamesPath = os.path.join(SteamPath, 'steamapps', 'common')
    except WindowsError:
        pass
