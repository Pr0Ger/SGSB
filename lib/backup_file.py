import tarfile
import os


class BackupFile(object):

    def __init__(self, Name, write):
        if write:
            self.__file = tarfile.open(os.path.join('.', 'backups', Name + '.tar.bz2'), 'w:bz2')
        else:
            self.__file = tarfile.open(os.path.join('.', 'backups', Name + '.tar.bz2'), 'r:bz2')

    def __del__(self):
        self.__file.close()

    def add_files(self, id, path, files):
        if isinstance(files, str):
            files = [files]

        for it in files:
            if os.path.exists(os.path.join(path, it)):
                print(' backuping file {}'.format(it))
                archive_name = "data/{}/{}".format(id, it)
                self.__file.add(os.path.join(path, it), archive_name)

    def add_folder(self, id, path):
        raise NotImplementedError

    def restore_files(self, id, path, files):
        if not os.path.exists(path):
            os.makedirs(path)
        if isinstance(files, str):
            files = [files]

        for it in files:
            archive_name = "data/{}/{}".format(id, it)
            try:
                current_file = self.__file.getmember(archive_name)
                print(' restoring file {}'.format(it))
                current_file.name = current_file.name[(6 + len(id)):]
                self.__file.extract(current_file, path)
            except KeyError:
                pass
