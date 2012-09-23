#!/usr/bin/env bash

SCRIPT_PATH="$( cd -P "$( dirname "$0" )" && pwd )"

if [ ! -d web ]
then
    echo "changing directory..."
    cd $SCRIPT_PATH/..
fi

tempfile="/tmp/hold`date +%Y%j%H%M%S%N`"

search=`grep "SERVICE_VERSION = " services/config/__init__.py`
replace="SERVICE_VERSION = 'v`date +%Y%j`'"

echo $search
echo $replace
sed "s/${search}/${replace}/g" services/config/__init__.py > $tempfile && mv $tempfile services/config/__init__.py




