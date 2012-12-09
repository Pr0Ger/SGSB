import os
import platform


MyDocumentsPath = None
SavedGamesPath = None
SteamGamesPath = None

if platform.system() == 'Windows':
    import ctypes
    from ctypes.wintypes import MAX_PATH

    dll = ctypes.windll.shell32
    buf = ctypes.create_unicode_buffer(MAX_PATH + 1)
    if dll.SHGetSpecialFolderPathW(None, buf, 0x0005, False):
        MyDocumentsPath = os.path.normcase(buf.value)

    from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx

    try:
        key = OpenKey(HKEY_CURRENT_USER, 'Software\\Valve\\Steam')
        SteamPath = QueryValueEx(key, 'SteamPath')[0]
        SteamGamesPath = os.path.normcase(os.path.join(SteamPath, 'steamapps', 'common'))
    except WindowsError:
        pass

    profile_path = os.environ['USERPROFILE']

    _ = os.path.join(profile_path, 'Saved Games')
    if os.path.isdir(_):
        SavedGamesPath = _

if platform.system() == 'Darwin':

    MyDocumentsPath = os.path.expanduser(os.path.join('~', 'Documents'))
