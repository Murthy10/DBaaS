# DBaaS

## postgraphile
Plugins:
  * postgraphile-plugin-connection-filter
  * @graphile/postgis
  * @graphile-contrib/pg-order-by-related
  * @graphile/pg-aggreates

### Notes
  * ORDER BY multiple columns -> @graphile-contrib/pg-order-by-related
  * GROUP BY not possible -> Views
  * SUM not possible -> Views (wip @graphile/pg-aggreates)
  * Nested Queries not possible -> View (7a..)


##
```bash
{
  allActors(filter: {firstName: {includes: "a"}}) {
    nodes {
      firstName
      lastName
    }
  }
}
```