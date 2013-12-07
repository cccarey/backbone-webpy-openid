define([
    'jquery',
    'lib/underscore',
    'lib/backbone',
    'lib/handlebars',
    'views/main_layout',
    'views/header',
    'views/login',
    'views/user'
], function($, _, Backbone, Handlebars, mainLayout, header, loginPage, userPage) {
    'use strict';

    Backbone.View.prototype.close = function() {
        this.remove();
        this.unbind();
        if (this.onClose) {
            this.onClose();
        }
    };

    return { mainLayout: mainLayout, header: header, loginPage: loginPage, userPage: userPage };

});
