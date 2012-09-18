import tarfile
import os


class BackupFile(object):

    def __init__(self, Name, write):
        restricted_characters = '/\\?%*:|"<>'
        Name = ''.join(filter(lambda x: x not in restricted_characters, Name))
        if write:
            self.__file = tarfile.open(os.path.join('.', 'backups', Name + '.tar.bz2'), 'w:bz2', encoding='utf-8')
        else:
            self.__file = tarfile.open(os.path.join('.', 'backups', Name + '.tar.bz2'), 'r:bz2', encoding='utf-8')

    def __del__(self):
        self.__file.close()

    def __add_file(self, archive_path, full_path, depth=0):
        for it in os.listdir(full_path):
            new_archive_path = '/'.join([archive_path, it])
            new_full_path = os.path.join(full_path, it)

            if os.path.isdir(os.path.join(full_path, it)):
                print(' ' * depth, ' {}/'.format(it))
                self.__add_file(new_archive_path, new_full_path, depth + 1)
            else:
                print(' ' * depth, ' {}'.format(it))
                self.__file.add(new_full_path, new_archive_path)

    def add_files(self, id, path, files):
        if isinstance(files, str):
            files = [files]

        for it in files:
            if os.path.exists(os.path.join(path, it)):
                print(' backuping file {}'.format(it))
                archive_name = "data/{}/{}".format(id, it)
                self.__file.add(os.path.join(path, it), archive_name)

    def add_folder(self, id, path, folder):
        full_path = os.path.join(path, folder)
        if os.path.exists(full_path):
            print(' backuping folder {}'.format(full_path))
            archive_name = "data/{}".format(id)
            self.__add_file(archive_name, full_path)

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

    def restore_folder(self, id, path, folder):
        full_path = os.path.join(path, folder)
        print(' restoring folder {}'.format(full_path))

        if not os.path.exists(full_path):
            os.makedirs(full_path)

        archive_name = "data/{}".format(id)

        subdir_and_files = []
        for it in self.__file.getmembers():
            if it.name.startswith(archive_name):
                it.name = it.name[(6 + len(id)):]
                subdir_and_files.append(it)

        self.__file.extractall(full_path, subdir_and_files)
