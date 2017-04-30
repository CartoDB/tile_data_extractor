import csv
import StringIO
from tile_data_extractor.presenters.presenter import DataPresenter

class DataCSVPresenter(DataPresenter):

    FIELDS = ['host', 'database', 'user', 'tables',
              'timestamp', 'duration', 'bbox', 'x',
              'y', 'z', 'query', 'update', 'basemaps']

    def format(self, data):
        csv_data = None
        try:
            io_writer = StringIO.StringIO()
            csv_writer = csv.DictWriter(io_writer, self.FIELDS)
            csv_data = self.__prepare_data(data)
            csv_writer.writerow(csv_data)
            return io_writer.getvalue()
        except Exception as e:
            print 'Error writing csv: {0} --- data: {1}'.format(e, csv_data)

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
        if not data['update']:
            formatted_data['x'] = int(data['x'])
            formatted_data['y'] = int(data['y'])
            formatted_data['z'] = int(data['z'])
        formatted_data['query'] = data['query'].encode('ascii', 'replace')
        formatted_data['update'] = data['update']
        formatted_data['basemaps'] = data['basemaps']
        return formatted_data
