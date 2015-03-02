#!/usr/bin/env bash

TARGET="/tmp/app-test"
[[ ! -z "$1" ]] && TARGET="$1"

[[ ! -d "$TARGET" ]] && mkdir "$TARGET"

cp -r services "$TARGET"
cp -r web "$TARGET"

find "$TARGET" -name "*.pyc" -exec rm -f {} \;
find "$TARGET" -name "start-dev.sh" -exec rm -f {} \;