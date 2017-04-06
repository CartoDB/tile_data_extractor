import csv
import StringIO
from tile_data_extractor.presenters.presenter import DataPresenter

class DataCSVPresenter(DataPresenter):

    FIELDS = ['host', 'database', 'user', 'tables',
              'timestamp', 'duration', 'bbox', 'x',
              'y', 'z', 'query', 'update', 'basemaps']

    def format(self, data):
        io_writer = StringIO.StringIO()
        csv_writer = csv.DictWriter(io_writer, self.FIELDS)
        csv_writer.writerow(self.__prepare_data(data))
        return io_writer.getvalue()

    def get_header(self):
        return ",".join(self.FIELDS)

    def __prepare_data(self, data):
        formatted_data = {}
        formatted_data['host'] = data['host']
        formatted_data['database'] = data['database']
        formatted_data['user'] = data['user']
        formatted_data['tables'] = "{{{0}}}".format(",".join(data['tables']))
        formatted_data['timestamp'] = data['timestamp']
        formatted_data['duration'] = data['duration']
        formatted_data['bbox'] = data['bbox']
        formatted_data['x'] = int(data['x'])
        formatted_data['y'] = int(data['y'])
        formatted_data['z'] = int(data['z'])
        formatted_data['query'] = data['query']
        formatted_data['update'] = data['update']
        formatted_data['basemaps'] = data['basemaps']
        return formatted_data
