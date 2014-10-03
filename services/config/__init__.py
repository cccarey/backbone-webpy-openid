import web, auth
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from social.utils import setting_name
from social.apps.webpy_app import app as social_app

db_settings = {
	"drv_name": "mysql",
	"user": "bwouser",
	"password": "test123",
	"database": "bwoapp",
	"server": "localhost"
}

db = web.database(
	dbn=db_settings["drv_name"],
	user=db_settings["user"],
	pw=db_settings["password"],
	db=db_settings["database"]
	)

engine = create_engine(
	"%s://%s:%s@%s/%s" % (
		db_settings["drv_name"],
		db_settings["user"],
		db_settings["password"],
		db_settings["server"],
		db_settings["database"]
		)
	)

settings = {
    "version": "v2014228",
    "app": "/openid",
    "profile.edit": "/openid",
    "basedir": "/openid"
}

URLS = (
    '/info', 'app.info.root',
    '/user', 'app.user.root',
    '/logout', 'app.user.logout',
    '', social_app.app_social
)

oauth2_key = os.getenv('GOOGLE_OAUTH2_KEY', 'key not set')
oauth2_secret = os.getenv('GOOGLE_OAUTH2_SECRET', 'secret not set')

def setup_social_auth():
	web.config[setting_name('GOOGLE_OAUTH2_KEY')] = oauth2_key
	web.config[setting_name('GOOGLE_OAUTH2_SECRET')] = oauth2_secret
	web.config[setting_name('USER_MODEL')] = 'models.user.User'
	web.config[setting_name('AUTHENTICATION_BACKENDS')] = (
	    'social.backends.google.GoogleOAuth2',
	    )
	# TODO: change following two lines on deployment
	web.config[setting_name('NEW_USER_REDIRECT_URL')] = 'http://localhost:8080/openid/#/edit'
	web.config[setting_name('LOGIN_REDIRECT_URL')] = 'http://localhost:8080/openid'
	web.config[setting_name('SANITIZE_REDIRECTS')] = False

def create_web_session(web_app):
	# Test is a workaround to prevent debug reloader from creating a second version
	# See http://webpy.org/cookbook/session_with_reloader
	if not hasattr(web, "web_session"):
	    session = web.session.Session(web_app, web.session.DBStore(db, 'sessions'), {'count':0})
	    web.web_session = session

	return web.web_session

def create_db_session():
	# Test is a workaround to prevent debug reloader from creating a second version
	# See http://webpy.org/cookbook/session_with_reloader
	if not hasattr(web, "db_session"):

		Session = sessionmaker(bind=engine)
		Session.configure(bind=engine)

		web.db_session = Session()

	return web.db_session

def migrate_model():
	from models.user import Base
	from social.apps.webpy_app.models import SocialBase

	Base.metadata.create_all(engine)
	SocialBase.metadata.create_all(engine)

def load_sqla(handler):
    web.ctx.orm = scoped_session(sessionmaker(bind=engine))
    try:
        return handler()
    except web.HTTPError:
        web.ctx.orm.commit()
        raise
    except:
        web.ctx.orm.rollback()
        raise
    finally:
        web.ctx.orm.commit()
        # web.ctx.orm.expunge_all()
