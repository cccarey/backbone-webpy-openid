# −*− coding: UTF−8 −*−

import web

class AuthError(Exception): pass

def protected(**pars):
    def decorator(func):
        def proxyfunc(iself, *args, **kw):
            try:
                if not web.web_session.logged_in:
                    raise AuthError

            except (AttributeError, AuthError):
                web.ctx.status = '401'
                return "Not Authenticated"

            return func(iself, *args, **kw)
        return proxyfunc
    return decorator
