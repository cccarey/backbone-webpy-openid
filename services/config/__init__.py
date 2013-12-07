import web, auth

db = web.database(dbn='mysql', user='bwouser', pw='test123', db='bwoapp')

settings = {
    "version": "v2012309",
    "app": "/openid",
    "profile.edit": "/openid",
    "basedir": "/openid"
}

URLS = (
    '/info', 'app.info.root',
    '/user', 'app.user.root',
    '/login', 'app.user.openidLoginStart',
    '/loginComplete', 'app.user.openidLoginComplete',
    '/logout', 'app.user.logout'
)

