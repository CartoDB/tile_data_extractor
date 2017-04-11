CREATE EXTENSION pgcrypto;

CREATE TABLE tile_data (
    id uuid DEFAULT gen_random_uuid(),
    host varchar(100),
    database varchar(100),
    username varchar(100),
    tables text[],
    executed_at timestamp,
    duration decimal,
    bbox varchar(256),
    x integer,
    y integer,
    z integer,
    query text,
    is_update boolean default false,
    is_basemaps boolean default false,
    PRIMARY KEY(id)
);

CREATE INDEX idx_timestamp on tile_data ("executed_at");
CREATE INDEX idx_bbox on tile_data ("bbox");
CREATE INDEX idx_tables on tile_data USING GIN ("tables");