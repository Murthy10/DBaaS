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

Used plugins:
  * postgraphile-plugin-connection-filter
  * @graphile/postgis
  * @graphile-contrib/pg-order-by-related
  * @graphile/pg-aggreates