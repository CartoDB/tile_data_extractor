
--------------------------------------
-- this sql gets stats per user about the time spent rendering vs the time wasted
--------------------------------------

-- users with repeated tiles
-- select username from (select username, count(1) from tile_data where not is_update group by bbox, username, tables) a where count > 1 group by 1;
with tile_data_with_last_update as (
    select td.*, last_update.count, last_update.sum, last_update.id idd from tile_data td, lateral (
        with lu as (
            SELECT * from (
                (
                    select id, executed_at from tile_data t where t.is_update and t.executed_at < td.executed_at 
                    and t.username = td.username and t.tables && td.tables
                    order by executed_at asc limit 1
                )
                UNION ALL
                (
                    SELECT gen_random_uuid(), '1990-01-01'::timestamp
                )
            ) __ limit 1
        )
        select count(1), sum(tt.duration), array_agg(lu.id) id from tile_data tt, lu where tt.executed_at > COALESCE(lu.executed_at, '1990-01-01'::timestamp)  and tt.executed_at <= td.executed_at 
        and tt.bbox = td.bbox and
        tt.username = td.username and
        tt.tables = td.tables

    ) last_update 
    order by executed_at asc
),
aa as (
    select bbox, tables, username, duration, last_value(sum) over (partition by bbox, username, tables order by count) from tile_data_with_last_update where count >= 2
),
bb as (
    select username, max(last_value), max(last_value) - avg(duration) over_render, sum(duration)  from aa group by bbox, tables, username
),
cc as (
    select username, sum(duration) sum_total from tile_data where not is_update group by username
),
dd as (
select username, sum(over_render) sum_overrender from bb group by username
)
-- calculates the time spent on rendering vs the time rendering tiles that shouldnt have been rendered
select dd.username, sum_total, sum_overrender from dd join cc on cc.username = dd.username;

-- these are tests
--select bbox, tables, username, duration, sum, count, idd from tile_data_with_last_update;
--select 
    --count(1) filter (where count >=2),
    --sum(sum) filter (where count >=2),
    --count(1) filter (where count < 2),
    --sum(sum) filter (where count < 2),
    --sum(sum)
    --from tile_data_with_last_update where not is_update;
--select username from tile_data_with_last_update where count >= 2 group by 1;
--select username, sum(duration) from aa group by username;

