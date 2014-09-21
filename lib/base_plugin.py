import dropbox
import os
import platform
from .backup_file import BackupFile


class BasePlugin(object):
    Name = "Undefined"
    Author = "Pr0Ger"
    current_os = platform.system()
    dependencies = []
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

        backups_dropbox = []
        if os.path.exists('.dropbox_access_token'):
            access_file = open('.dropbox_access_token', 'r')
            access_token = access_file.read()
            dropbox_client = dropbox.client.DropboxClient(access_token)

            root_folder = dropbox_client.metadata('/')
            for it in root_folder['contents']:
                backups_dropbox.append(it['path'][1:])

        if not os.path.exists(os.path.join('.', 'backups', backup_name + '.tar.xz')) and \
           not backup_name + '.tar.xz' in backups_dropbox:
            print('Unable to find backup for {}.'.format(self.Name))
            raise IOError
        print('Restoring {}...'.format(self.Name))

    def init(self):
        pass

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
