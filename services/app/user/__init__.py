import web, json

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
        return json.dumps(AlchemyToJSON(user))
        
class logout:
    def GET(self):
        web.web_session.kill()
        return "{\"success\":\"true\"}"
