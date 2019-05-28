createdb -U postgres sakila
psql -U postgres -d sakila -f /sakila.sql
psql -U postgres -d sakila -f /sakila_views.sql