var AppController = {
    init: function() {
        this.model = new AppModel();
        this.view = new AppView({model: this.model});
        this.view.render();
        return this;
    }
};
