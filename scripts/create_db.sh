#!/usr/bin/env bash

DBNAME=""
DBUSER=""
DBPASSWD=""
DBPASSCHK="check"

[[ -z "$1" ]] || DBNAME="$1"
[[ -z "$2" ]] || DBUSER="$2"
[[ -z "$3" ]] || {
    DBPASSWD="$3"
    DBPASSCHK="$3"
}

[[ -z "$DBNAME" ]] || {
    echo -n "Enter db name    : "
    read DBNAME
}
[[ -z "$DBUSER" ]] || {
    echo -n "Enter db user    : "
    read DBUSER
}

while [ "$DBPASSWD" != "$DBPASSCHK" ]; do
    echo -n "Enter db password: "
    read -s DBPASSWD
    echo

    echo -n "Re-enter password: "
    read -s DBPASSCHK
    echo
done

echo "creating $DBNAME database with user $DBUSER..."
echo -n "MySQL root user -> "
mysql -u root -p << END
    create database if not exists $DBNAME;
    grant all privileges on $DBNAME.* to '$DBUSER'@'localhost' identified by '$DBPASSWD' with grant option;
    flush privileges;
END
