import web

from config import *
from app import *

import auth
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
        user = web.db_session.query(models.user.User).get(web.web_session.user_id)
        return user.toJSON()

    @auth.protected()
    def PUT(self):
    	user = web.db_session.query(models.user.User).get(web.web_session.user_id)
        data = web.utils.Storage(json.JSONDecoder().decode(web.data()))
        update_user = models.user.User(**data)
        web.db_session.merge(update_user)
        web.db_session.commit()
        
        return update_user.toJSON()

class logout:
    def GET(self):
        web.web_session.kill()
        return "{\"success\":\"true\"}"
