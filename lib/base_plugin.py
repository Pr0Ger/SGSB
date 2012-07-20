import os
import platform
from .backup_file import BackupFile


class BasePlugin(object):
    Name = "Undefined"
    Author = "Pr0Ger"
    current_os = platform.system()
    support_os = []

    def backup(self):
        if not self.detect():
            print('Game {} isn\'t installed.'.format(self.Name))
            raise IOError
        print('Backuping {}...'.format(self.Name))

    def detect(self):
        raise NotImplementedError

    def restore(self):
        if not os.path.exists(os.path.join('.', 'backups', self.Name + '.tar.bz2')):
            print('Unable to find backup for {}.'.format(self.Name))
            raise IOError
        print('Restoring {}...'.format(self.Name))

    @property
    def available(self):
        return self.current_os in self.support_os

    @property
    def backup_file(self):
        return BackupFile(self.Name, True)

    @property
    def restore_file(self):
        return BackupFile(self.Name, False)
