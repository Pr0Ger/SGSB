import os
import platform
from .backup_file import BackupFile


class BasePlugin(object):
    Name = "Undefined"
    Author = "Pr0Ger"
    current_os = platform.system()
    support_os = []

    def __init__(self):
        self.archive_file = None

    def backup(self):
        if not self.detect():
            print('Game {} isn\'t installed.'.format(self.Name))
            raise IOError
        print('Backuping {}...'.format(self.Name))

    def detect(self):
        raise NotImplementedError

    def restore(self):
        restricted_characters = '/\\?%*:|"<>'
        backup_name = ''.join(filter(lambda x: x not in restricted_characters, self.Name))
        if not os.path.exists(os.path.join('.', 'backups', backup_name + '.tar.bz2')):
            print('Unable to find backup for {}.'.format(self.Name))
            raise IOError
        print('Restoring {}...'.format(self.Name))

    @property
    def available(self):
        return self.current_os in self.support_os

    @property
    def backup_file(self):
        if self.archive_file:
            return self.archive_file
        else:
            self.archive_file = BackupFile(self.Name, True)
            return self.archive_file

    @property
    def restore_file(self):
        if self.archive_file:
            return self.archive_file
        else:
            self.archive_file = BackupFile(self.Name, False)
            return self.archive_file
