import web, config

class root:
    def GET(self):
        web.header('Content-Type', 'application/json')
        return "{ \"version\": \"%s\", \"data\": \"%s\" }" % (
        	config.settings["version"], 
        	web.web_session._data
        	)
