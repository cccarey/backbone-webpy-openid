#!/usr/bin/env bash
getfile() {
    wget $1/$2
    mv $2 web/js/lib/$3
}

function process() {
    while [ ! -z "$1" ]
    do
        url="$1"
        file="$2"
        new_file="$3"
        getfile $url $file $new_file

        shift 3
    done
}

files="http://requirejs.org/docs/release/2.1.9/minified require.js require.js
https://raw.github.com/requirejs/text/latest text.js text.js
http://backbonejs.org backbone.js backbone.js
http://underscorejs.org underscore.js underscore.js
http://code.jquery.com jquery-2.0.3.js jquery-2.0.3.js
http://builds.handlebarsjs.com.s3.amazonaws.com handlebars-v1.1.2.js handlebars.js"

process $files
