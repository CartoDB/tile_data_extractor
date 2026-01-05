# ⚠️ ARCHIVED - This repository is no longer maintained

**This repository has been archived and is no longer actively maintained.**

This project was last updated on 2017-05-16 and is preserved for historical reference only.

- 🔒 **Read-only**: No new issues, pull requests, or changes will be accepted
- 📦 **No support**: This code is provided as-is with no support or updates
- 🔍 **For reference only**: You may fork this repository if you wish to continue development

For current CARTO projects and actively maintained repositories, please visit: https://github.com/CartoDB

---

# Tile queries data extractor
Python library that process PostgreSQL logs and extract tile data from mapnik queries

## Data extracted
- XYZ
- Database name
- Database user
- Timestamp
- Duration of the query
- Tables used or basemap functions called
- Is a basemap query?
- Is an update action query?

## Proccesed line example

```json
{"tables": ["buildings_zoomed"], "database": "cartodb_user_01df4999-81aa-4135-b460-1e5b8a7f7f79_db", "timestamp": "2017-02-09 08:19:13", "xyz": {"y": 8705.0, "x": 18900.0, "z": 15.0}, "update": false, "user": "cartodb_user_01df4999-81aa-4135-b460-1e5b8a7f7f79", "duration": "0.774", "basemaps": true}
```

## Example of usage

```python
#!/usr/bin/python

from tile_data_extractor.repositories import FileRepository
from tile_data_extractor.services import TileDataExtractionService


repository = FileRepository('/tmp/basemaps_processed.log')
service = TileDataExtractionService(repository)
service.process('/home/ubuntu/www/misc/basemaps_research/logs/postgresql_50mb.log')
```

## How to process log files and import them into your database

Now you could use [the provided script](https://github.com/CartoDB/tile_data_extractor/blob/master/bin/tile_data_generator.py) to generate a CSV file to import into the database:
```bash
python tile_data_generator.py file1.log file2.log...fileN.log --output /output/dir --format csv
```
[Here](https://github.com/CartoDB/tile_data_extractor/blob/master/tools/tables.sql) you have a SQL with the table creation script. Once you have the table created you can import the generated CSV into your table using:

```sql
COPY tile_data (host, database, username, tables, executed_at, duration, bbox, x, y, z, query, is_update, is_basemaps) FROM '/path/to/file.csv' WITH CSV HEADER;
```

## FAQ

- What is the use of the update column?

  We need to register any update, delete or insert queries tables because this
  queries trigger cache invalidations and we want to take them into account
