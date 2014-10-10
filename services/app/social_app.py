'''
This is a modified version of social.apps.webpy_app.app from the 
python-social-auth package (v0.2.2-dev).

This file adds the ability to insert a path prefix on the 'complete'
path in the event this is not hosted at the root domain.

In order to insert a path prefix, add an environment variable called
'PATH_PREFIX' with the prefix required. The value of this prefix must
include a leading slash.

- ccarey - 2014-10-10
'''
import web

from social.actions import do_auth, do_complete, do_disconnect
from social.apps.webpy_app.utils import psa, load_strategy

import os

path_prefix = os.getenv("PATH_PREFIX", "")
complete_path = '%s/complete/%%(backend)s/' % path_prefix

urls = (
  '/login/(?P<backend>[^/]+)/?', 'auth',
  '/complete/(?P<backend>[^/]+)/?', 'complete',
  '/disconnect/(?P<backend>[^/]+)/?', 'disconnect',
  '/disconnect/(?P<backend>[^/]+)/(?P<association_id>\d+)/?', 'disconnect',
)


class BaseViewClass(object):
    def __init__(self, *args, **kwargs):
        self.session = web.web_session
        method = web.ctx.method == 'POST' and 'post' or 'get'
        self.strategy = load_strategy()
        self.data = web.input(_method=method)
        super(BaseViewClass, self).__init__(*args, **kwargs)

    def get_current_user(self):
        if not hasattr(self, '_user'):
            if self.session.get('logged_in'):
                self._user = self.strategy.get_user(
                    self.session.get('user_id')
                )
            else:
                self._user = None
        return self._user

    def login_user(self, user):
        self.session['logged_in'] = True
        self.session['user_id'] = user.id


class auth(BaseViewClass):
    def GET(self, backend):
        return self._auth(backend)

    def POST(self, backend):
        return self._auth(backend)

    @psa(complete_path)
    def _auth(self, backend):
        return do_auth(self.backend)


class complete(BaseViewClass):
    def GET(self, backend, *args, **kwargs):
        return self._complete(backend, *args, **kwargs)

    def POST(self, backend, *args, **kwargs):
        return self._complete(backend, *args, **kwargs)

    @psa(complete_path)
    def _complete(self, backend, *args, **kwargs):
        return do_complete(
            self.backend,
            login=lambda backend, user, social_user: self.login_user(user),
            user=self.get_current_user(), *args, **kwargs
        )


class disconnect(BaseViewClass):
    @psa()
    def POST(self, backend, association_id=None):
        return do_disconnect(self.backend, self.get_current_user(),
                             association_id)


app_social = web.application(urls, locals())
