#!/usr/bin/env bash
getfile() {
    wget $1
    mv $2 web/js/lib
}

function process() {
    while [ ! -z "$1" ]
    do
        url="$1"
        file="$2"
        echo "Url: $url -> File: $file"
        getfile $url $file

        shift 2
    done
}

files="http://requirejs.org/docs/release/2.1.9/minified/require.js require.js
https://raw.github.com/requirejs/text/latest/text.js text.js
http://backbonejs.org/backbone.js backbone.js
http://underscorejs.org/underscore.js underscore.js
http://code.jquery.com/jquery-2.0.3.js jquery-2.0.3.js"

process $files
