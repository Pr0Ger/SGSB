import dropbox
import tarfile
import os
import sys
from tempfile import TemporaryFile
from lib.chunked_uploader import ChunkedProgressUploader


class BackupFile(object):

    def __init__(self, Name, write):
        restricted_characters = '/\\?%*:|"<>'
        Name = ''.join(filter(lambda x: x not in restricted_characters, Name))

        self.__write = write
        self.__dropbox_client = None
        if os.path.exists('.dropbox_access_token'):
            access_file = open('.dropbox_access_token', 'r')
            access_token = access_file.read()
            self.__dropbox_client = dropbox.client.DropboxClient(access_token)

        if write:
            if self.__dropbox_client:
                self.__tmp_file = TemporaryFile()
                self.__file_name = '/%s.tar.xz' % (Name,)

                self.__file = tarfile.open(mode='w:xz', fileobj=self.__tmp_file, encoding='utf-8')
            else:
                self.__file = tarfile.open(os.path.join('.', 'backups', Name + '.tar.xz'), 'w:xz', encoding='utf-8')
        else:
            if self.__dropbox_client:
                remote_file = self.__dropbox_client.get_file('/%s.tar.xz' % (Name,))
                self.__tmp_file = TemporaryFile()
                self.__tmp_file.write(remote_file.read())
                self.__tmp_file.seek(0)

                self.__file = tarfile.open(mode='r:xz', fileobj=self.__tmp_file, encoding='utf-8')
            else:
                self.__file = tarfile.open(os.path.join('.', 'backups', Name + '.tar.xz'), 'r:xz', encoding='utf-8')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file.close()

        self.__tmp_file.seek(0)
        if self.__write and self.__dropbox_client:
            sys.stdout.write(' uploading to Dropbox... (0%)')
            sys.stdout.flush()

            size = os.fstat(self.__tmp_file.fileno()).st_size
            uploader = ChunkedProgressUploader(self.__dropbox_client, self.__tmp_file, size)

            for offset in uploader.upload_chunked():
                sys.stdout.write('\r uploading to Dropbox... ({0:f}%)'.format(offset / size * 100))
                sys.stdout.flush()

            uploader.finish(self.__file_name, overwrite=True)

            print()

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
