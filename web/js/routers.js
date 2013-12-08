define([
    'jquery',
    'lib/underscore',
    'lib/backbone',
    'config',
    'views/loader',
    'models/loader'
], function($, _, Backbone, config, views, models) {
    'use strict';

    return {
        OpenIdRouter: Backbone.Router.extend({
            routes: {
                '' : 'showUser',
                'logout' : 'processLogout',
                'login' : 'showLogin'
            },

            initialize: function() {
                this.info = new models.info({});
                this.user = new models.user({ onNoAuth: this.onNoAuth });
                this.pageInfo = new models.pageInfo({ app: "Backbone/webpy/OpenID" });

                this.mainLayout = new views.mainLayout({ info: this.info, user: this.user, pageInfo: this.pageInfo });
            },

            /* --- helper functions --- */

            onNoAuth: function() {
                this.user.clear();
                this.navigate("login", { trigger: true });
            },

            /* --- router functions --- */

            processLogout: function() {
                this.user.clear();
                $.ajax({
                    url: config.apiBase + "logout",
                    type: "GET",
                    success: function() { window.location = "./#/login"; }
                });
            },

            showUser: function() {
                this.mainLayout.show(new views.userPage({ model: this.user, pageInfo: this.pageInfo }));
            },

            showLogin: function() {
                this.mainLayout.show(new views.loginPage({ pageInfo: this.pageInfo }));
            }
        })
    };
});