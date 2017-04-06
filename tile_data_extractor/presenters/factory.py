
from tile_data_extractor.presenters.csv_presenter import DataCSVPresenter
from tile_data_extractor.presenters.json_presenter import DataJSONPresenter

class DataPresenterFactory(object):

    @classmethod
    def build(cls, format):
        if format == 'csv':
            return DataCSVPresenter()
        elif format == 'json':
            return DataJSONPresenter()
        else:
            raise NotImplementedError('Selected format for presenter doesn\'t exists')
