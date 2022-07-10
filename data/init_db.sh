#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER tarik;
    CREATE DATABASE port_list;
    GRANT ALL PRIVILEGES ON DATABASE port_list TO tarik;
EOSQL

psql -v 'ON_ERROR_STOP=1' -d port_list -f ./data/dump.sql