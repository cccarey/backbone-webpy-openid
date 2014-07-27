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

from config import db, create_web_session, create_db_session, load_sqla, setup_social_auth, \
				   migrate_model
from config.updateDB import UpdateDB
dbUpdate = UpdateDB(db)

setup_social_auth()
migrate_model()
session = create_web_session(web_app)
db_session = create_db_session()

web_app.add_processor(load_sqla)

if __name__ == "__main__":
    web_app.run()

application = web_app.wsgifunc()

