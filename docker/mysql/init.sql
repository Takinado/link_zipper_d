CREATE DATABASE link_zipper_dj_db CHARACTER SET utf8 COLLATE utf8_bin;

CREATE USER mysql_user WITH PASSWORD 'mysql_password';

ALTER ROLE mysql_user SET client_encoding TO 'utf8';
-- ALTER ROLE mysql_user SET default_transaction_isolation TO 'read committed';
-- ALTER ROLE mysql_user SET timezone TO 'GMT+3';

GRANT ALL PRIVILEGES ON DATABASE link_zipper_dj_db TO mysql_user;