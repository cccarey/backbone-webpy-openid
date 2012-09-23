import web, config

class root:
    def GET(self):
        web.header('Content-Type', 'application/json')
        return "{ \"version\": \"%s\" }" % config.SERVICE_VERSION

