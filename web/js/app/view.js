var UserView = Backbone.View.extend({
    el: "#header",
    
    events: {
        "click #logout" : "handleLogoutClick"
    },
    
    initialize: function() {
        _.bindAll(this, "render", "handleLogoutClick");
        this.model.bind("change", this.render);
    },
    
    render: function() {
        $(this.el).html(ich.header_frag(this.model.toJSON()));
        return this;
    },
    
    handleLogoutClick: function() { app.logoutClick(); }
});

var AppView = Backbone.View.extend({
    initialize: function() {
        this.userView = new UserView({model:this.model.user});
    },
    
    render: function() {
        return this;
    },
});
