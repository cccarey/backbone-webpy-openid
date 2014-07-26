#!/usr/bin/env python
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)

# following line lets web.seeother work so it does not include the
# name of this file
os.environ['REAL_SCRIPT_NAME'] = ''

import web

from config import URLS

web_app = web.application(URLS, globals())

from config import db
from config.updateDB import UpdateDB
dbUpdate = UpdateDB(db)

if web.config.get('_session') is None:
    session = web.session.Session(web_app, web.session.DBStore(db, 'sessions'), {'count':0})
    web.config._session = session
else:
    session = web.config._session

if __name__ == "__main__":
    web_app.run()

application = web_app.wsgifunc()
