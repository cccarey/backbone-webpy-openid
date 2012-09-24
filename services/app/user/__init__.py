import web, config

class root:
    @config.auth.protected()
    def GET(self):
        web.header('Content-Type', 'application/json')
        web.ctx.status = '401'
