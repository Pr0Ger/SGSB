import os
import platform
from .backup_file import BackupFile


class BasePlugin(object):
    Name = "Undefined"
    Author = "Pr0Ger"
    current_os = platform.system()
    support_os = []

    def __init__(self):
        __old_backup_func = self.backup
        def __backup_closure():
            self.__backup()
            with self.backup_file() as _:
                __old_backup_func(_)

        self.backup = __backup_closure

        __old_restore_func = self.restore
        def __restore_closure():
            self.__restore()
            with self.restore_file() as _:
                __old_restore_func(_)

        self.restore = __restore_closure

    def __backup(self):
        if not self.detect():
            print('Game {} isn\'t installed.'.format(self.Name))
            raise IOError
        print('Backuping {}...'.format(self.Name))

    def __restore(self):
        restricted_characters = '/\\?%*:|"<>'
        backup_name = ''.join(filter(lambda x: x not in restricted_characters, self.Name))
        if not os.path.exists(os.path.join('.', 'backups', backup_name + '.tar.bz2')):
            print('Unable to find backup for {}.'.format(self.Name))
            raise IOError
        print('Restoring {}...'.format(self.Name))

    def backup(self, _):
        raise NotImplementedError

    def detect(self):
        raise NotImplementedError

    def restore(self, _):
        raise NotImplementedError

    def backup_file(self):
        return BackupFile(self.Name, True)

    def restore_file(self):
        return BackupFile(self.Name, False)

    @property
    def available(self):
        return self.current_os in self.support_os

