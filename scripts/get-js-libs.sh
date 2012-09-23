#!/usr/bin/env bash
getfile() {
    wget $1
    mv $2 web/js/lib
}

getfile "http://backbonejs.org/backbone-min.js" "backbone-min.js"
getfile "http://documentcloud.github.com/underscore/underscore-min.js" "underscore-min.js"
getfile "http://code.jquery.com/jquery.min.js" "jquery.min.js"

