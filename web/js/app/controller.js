var AppController = {
    init: function() {
        _.bindAll(this, "handleUnauthenticated", "logoutClick");
        this.model = new AppModel();
        this.view = new AppView({model: this.model});
        this.view.render();
        return this;
    },
    
    handleUnauthenticated: function() {
        window.location = "../";
    },
    
    logoutClick: function() {
        console.log("in logoutClick");
        $.ajax({
            url: "/backbone-webpy-openid-api/logout",
            type: "GET",
            success: function() {
                app.handleUnauthenticated();
            }
        });
        return false;
    }
};
