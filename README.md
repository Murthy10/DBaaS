# DBaaS
To use this repo you have to install docker and docker-compose on your system.
Further, python3.6 and pip is required.

Run the containers:
```bash
docker-compose build
docker-compose up
```

## postgraphile
Run: (previously, install the dependencies mentioned in the requirements.txt)
```bash
python3 graphql_requests.py
```


### Notes
  * ORDER BY multiple columns -> @graphile-contrib/pg-order-by-related
  * GROUP BY not possible -> Views
  * SUM not possible -> Views (wip @graphile/pg-aggreates)
  * Nested Queries not possible -> View (7a..)
  * Bad Docs!

Used plugins:
  * postgraphile-plugin-connection-filter
  * @graphile/postgis
  * @graphile-contrib/pg-order-by-related
  * @graphile/pg-aggreates (doesn't work until now)


## PostgREST
Run: (previously, install the dependencies mentioned in the requirements.txt)
```bash
python3 postgrest_requests.py
```


### Notes
  * Nice API Doc / Swagger (http://postgrest.org/en/v5.2/api.html)
  * Aggregations not possible (COUNT, SUM) -> Views
  * Nested Queries not possible -> Views
  * Multiple Join Filter results in null -> Change direction (7c)
  * No Geo-Spatial queries -> Views


## ToDo
 - [ ] pg_prewarm
 - [ ] average query time
 - [x] pgTune
 - [ ] osm_stops reference to didok_stops for postgraphile
 - [ ] ...