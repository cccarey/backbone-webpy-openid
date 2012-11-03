var UserView = Backbone.View.extend({
    el: "#header",
    
    initialize: function() {
        _.bindAll(this, "render");
        this.model.bind("change", this.render);
    },
    
    render: function() {
        console.log(this.model.get("first_name"));
        $(this.el).html(ich.header_frag(this.model.toJSON()));
        // this.delegateEvents(); // reattach events since we reset this.el
        return this;
    },
});

var AppView = Backbone.View.extend({
    initialize: function() {
        this.userView = new UserView({model:this.model.user});
    },
    
    render: function() {
        //this.el = this.userView.render().el;
        return this;
    },
});
