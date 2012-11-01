import web, auth

db = web.database(dbn='mysql', user='bwouser', pw='test123', db='bwoapp')

settings = {
    "version": "v2012267",
    "app": "/openid/app",
    "profile.edit": "/openid/app",
    "basedir": "/openid"
}        

URLS = (
    '/info', 'app.info.root',
    '/user', 'app.user.root',
    '/login', 'app.user.openidLoginStart',
    '/loginComplete', 'app.user.openidLoginComplete',
    '/logout', 'app.user.logout'
)

