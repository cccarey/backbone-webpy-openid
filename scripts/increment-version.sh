#!/usr/bin/env bash

SCRIPT_PATH="$( cd -P "$( dirname "$0" )" && pwd )"

if [ ! -d web ]
then
    echo "changing directory..."
    cd $SCRIPT_PATH/..
fi

tempfile="/tmp/hold`date +%Y%j%H%M%S%N`"

search=`grep "\"version\": \"" services/config/__init__.py`
replace="    \"version\": \"v`date +%Y%j`\","

echo $search
echo $replace
sed -i "s/${search}/${replace}/g" services/config/__init__.py




