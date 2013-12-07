require.config({
    paths: {
        jquery: 'lib/jquery-2.0.3',
        text: 'lib/text'
    },

    shim: {
        'lib/underscore': { exports: '_' },
        'lib/backbone': { deps: [ 'jquery', 'lib/underscore' ], exports: 'Backbone' },
        'lib/handlebars': { exports: 'Handlebars' }
    }
});

require([ 'routers' ], function(routers) {
    'use strict';

    $(document).ready(function() {
        var router = new routers.OpenIdRouter();
        Backbone.history.start();
    });
});
