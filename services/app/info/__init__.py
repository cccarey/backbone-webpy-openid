import web, json, config

class root:
    def GET(self):
        web.header('Content-Type', 'application/json')
        return json.dumps({
        	"version": config.settings["version"], 
        	"data":web.web_session._data.__dict__
        	})
