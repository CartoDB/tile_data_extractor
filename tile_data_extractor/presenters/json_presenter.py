import json
from presenter import DataPresenter

class DataJSONPresenter(DataPresenter):

    def format(self, data):
        return json.dumps(data)

    def get_header(self):
        return None
