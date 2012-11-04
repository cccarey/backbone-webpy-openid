var UserModel = Backbone.Model.extend({
    url: "/backbone-webpy-openid-api/user"
});

var AppModel = Backbone.Model.extend({
    initialize: function() {
        this.user = new UserModel();
        this.user.fetch({
            error: function(model, response) {
                console.log(response);
                if (response.status == 401) { app.handleUnauthenticated(); } 
            }
        });
    }
});


