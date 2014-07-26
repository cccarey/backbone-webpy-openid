import web, json

from config import *
from app import *

import models.user

import openid.consumer.consumer
import openid.store.memstore
import openid.extensions.ax

session = web.web_session
openidStore = openid.store.memstore.MemoryStore()

class root:
    @auth.protected()
    def GET(self):
        web.header('Content-Type', 'application/json')
        # web.ctx.status = '401'
        return json.dumps(auth.get_session_user())
        
class logout:
    def GET(self):
        auth.logout()
        return "{\"success\":\"true\"}"

class openidLoginStart:
    def GET(self):
        i = web.input()
        web.header('Content-Type', 'text/html')
        session['return_to'] = i.realm + i.openidEnd
        c = openid.consumer.consumer.Consumer(session, openidStore)
        a = c.begin('https://www.google.com/accounts/o8/id') # TODO: pass in the openid endpoint

        fetch_request = openid.extensions.ax.FetchRequest()
        fetch_request.add(openid.extensions.ax.AttrInfo(
                "http://schema.openid.net/contact/email", 
                count=openid.extensions.ax.UNLIMITED_VALUES, 
                required=True)
            )
        fetch_request.add(openid.extensions.ax.AttrInfo(
                "http://axschema.org/namePerson/first", 
                count=openid.extensions.ax.UNLIMITED_VALUES, 
                required=True)
            )
        fetch_request.add(openid.extensions.ax.AttrInfo(
                "http://axschema.org/namePerson/last", 
                count=openid.extensions.ax.UNLIMITED_VALUES, 
                required=True)
            )
        a.addExtension(fetch_request)
        
        return a.htmlMarkup(i.realm, session.return_to)
        
class openidLoginComplete:
    def GET(self):
        web.header('Content-Type', 'text/html')
        c = openid.consumer.consumer.Consumer(session, openidStore)
        new_user = False
        if 'return_to' in session:
            a = c.complete(web.input(), session['return_to'])
            del session['return_to']
            
            if a.status.lower() == 'success':
                fetch_response = openid.extensions.ax.FetchResponse.fromSuccessResponse(a)
                auth_user = {}
                auth_user['id_url'] = a.identity_url
                auth_user['user_id'] = -1
                auth_user['user_login'] = fetch_response.get("http://schema.openid.net/contact/email")[0]
                auth_user['first_name'] = fetch_response.get("http://axschema.org/namePerson/first")[0]
                auth_user['last_name'] = fetch_response.get("http://axschema.org/namePerson/last")[0]
                auth_user['nick_name'] = None
                # auth_user['is_admin'] = False
                auth_user = web.utils.Storage(auth_user)
                auth_user.is_admin = False
                
                user = models.user.get(user_login=auth_user.user_login)
                
                if user is None:
                    auth_user.id = models.user.save(auth_user)
                    new_user = True
                else:
                    auth_user.id = user.id
                    auth_user.nick_name = user.nick_name
                    auth_user.is_admin = user.is_admin
                    if user.id_url != auth_user.id_url:
                        new_user = True
                        models.user.save(auth_user, auth_user.id)

                auth.set_session_user(auth_user)
        
        if new_user:
            raise web.redirect(url="http://%s/%s" % (web.ctx.env["HTTP_X_FORWARDED_HOST"], settings["profile.edit"]))
            
        raise web.redirect(url="http://%s/%s" % (web.ctx.env["HTTP_X_FORWARDED_HOST"], settings["app"]))

