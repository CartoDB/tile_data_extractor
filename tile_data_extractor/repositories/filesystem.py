from repository import Repository

class FileRepository(Repository):

    def __init__(self, file_name):
        self.file_name = file_name

    def store(self, data):
        with open(self.file_name, 'ab') as f:
            f.write(data.strip('\r\n') + '\n' )
