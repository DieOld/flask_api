mysql -u root -p$MYSQL_ROOT_PASSWORD <<-EOSQL
CREATE TABLE feedbacks (ip VARCHAR(20), feedback INT(3));
EOSQL
