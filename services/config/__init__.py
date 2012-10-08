import web, auth

db = web.database(dbn='mysql', user='bwouser', pw='test123', db='bwoapp')

SERVICE_VERSION = 'v2012267'

URLS = (
    '/info', 'app.info.root',
    '/user', 'app.user.root',
    '/login', 'app.user.openidLoginStart',
    '/loginComplete', 'app.user.openidLoginComplete',
    '/logout', 'app.user.logout'
)

auth = auth.OpenIDAuth()

