# Tiles data extractor
Python library that used postgresql logs to extract tile data


## Example of usage

```python
#!/usr/bin/python

from tile_data_extractor.repositories import FileRepository
from tile_data_extractor.services import TileDataExtractionService


repository = FileRepository('/tmp/basemaps_processed.log')
service = TileDataExtractionService(repository)
service.process('/home/ubuntu/www/misc/basemaps_research/logs/postgresql_50mb.log')
```