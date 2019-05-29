createdb -U postgres eosm_ch
psql -U postgres -d eosm_ch -f /eosm_ch.sql
psql -U postgres -d eosm_ch -f /eosm_ch_fix.sql
psql -U postgres -d eosm_ch -f /eosm_views.sql
psql -U postgres -d eosm_ch -f /eosm_prewarm.sql

