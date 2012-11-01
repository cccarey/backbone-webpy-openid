var AppView = Backbone.View.extend({
    render: function() {
        this.el = ich.header(this.model.user.toJSON());
        this.delegateEvents(); // reattach events since we reset this.el
        return this;
    }
});
