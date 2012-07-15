import platform

MyDocumentsPath = None

if platform.system() == 'Windows':
    import ctypes
    from ctypes.wintypes import MAX_PATH

    dll = ctypes.windll.shell32
    buf = ctypes.create_unicode_buffer(MAX_PATH + 1)
    if dll.SHGetSpecialFolderPathW(None, buf, 0x0005, False):
        MyDocumentsPath = buf.value
