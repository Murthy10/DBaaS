createdb -U postgres eosm_ch
psql -U postgres -d eosm_ch -f /eosm_ch.sql
psql -U postgres -d eosm_ch -f /eosm_ch_fix.sql

