#!/usr/bin/env bash

if [ ! -z "$1" ]
then
    TARGET="$1"
else
    TARGET="/tmp/app-test"
fi

if [ ! -d "$TARGET" ]
then
    mkdir "$TARGET"
fi

cp -r services "$TARGET"

cp -r web "$TARGET"

rm -rf "$TARGET"/services/sessions
rm -f `find "$TARGET" -name "*.pyc"`

