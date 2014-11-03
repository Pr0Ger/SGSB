from dropbox.client import ChunkedUploader
from dropbox.client import ErrorResponse


class ChunkedProgressUploader(ChunkedUploader):

    def upload_chunked(self, chunk_size = 128 * 1024):

        while self.offset < self.target_length:
            next_chunk_size = min(chunk_size, self.target_length - self.offset)
            if self.last_block == None:
                self.last_block = self.file_obj.read(next_chunk_size)

            try:
                from io import BytesIO
                (self.offset, self.upload_id) = self.client.upload_chunk(
                    self.last_block, next_chunk_size, self.offset, self.upload_id)
                self.last_block = None
                yield self.offset
            except ErrorResponse as e:
                reply = e.body
                if "offset" in reply and reply['offset'] != 0:
                    if reply['offset'] > self.offset:
                        self.last_block = None
                        self.offset = reply['offset']
