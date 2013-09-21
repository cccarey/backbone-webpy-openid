#!/usr/bin/env bash
getfile() {
    wget $1
    mv $2 web/js/lib
}

getfile "http://backbonejs.org/backbone-min.js" "backbone.js"
getfile "http://documentcloud.github.com/underscore/underscore-min.js" "underscore.js"
getfile "http://code.jquery.com/jquery.min.js" "jquery.js"
getfile "https://github.com/andyet/ICanHaz.js/raw/master/ICanHaz.min.js" "ICanHaz.js"
