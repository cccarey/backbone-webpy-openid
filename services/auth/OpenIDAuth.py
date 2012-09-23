# −*− coding: UTF−8 −*−

import web, config
from web.session import SessionExpired

class AuthError(Exception): pass

class OpenIDAuth:
    def __init__(self, session=None):
        self.session = session
    
    def set_session(self, session):
        self.session = session
        
    def protected(self, **pars):
        """
        @protected([perm][, test])
        
        Decorator for limiting the access to pages.
        'perm' can be either a single permission (string) or a sequence
        of them.
        'test' must be a function that takes a user object and returns
        True or False.
        """
        def decorator(func):
            def proxyfunc(iself, *args, **kw):
                try:
                    openid_id = self.session.openid_id
                    email = self.session.email
                    
                    if openid_id is None:
                        raise AuthError
                        
                except (AttributeError, AuthError, SessionExpired):
                    raise web.seeother("/%s" % config.template.GLOBALS["basedir"])

                return func(iself, *args, **kw)
            return proxyfunc
        return decorator
    
    def is_authenticated(self):
        try:
            id = self.session.openid_id
            if id is None:
                return False
        except:
            return False
        return True

    def logout(self):
        self.session.kill()
              
    def set_session_user(self, user):
        self.session.user_id = user.id
        self.session.openid_id = user.id_url
        self.session.email = user.user_login
        self.session.first_name = user.first_name
        self.session.last_name = user.last_name
        self.session.nick_name = user.nick_name
        self.session.is_admin = user.is_admin

    def get_session_user(self):
        ret = dict()
        try:
            ret['user_id'] = self.session.user_id
            ret['id_url'] = self.session.openid_id
            ret['user_login'] = self.session.email
            ret['first_name'] = self.session.first_name
            ret['last_name'] = self.session.last_name
            ret['nick_name'] = self.session.nick_name
            ret['is_admin'] = self.session.is_admin
        except AttributeError:
            pass
        return web.utils.Storage(ret)
