# backbone-webpy-openid

OpenID user and login control using Backbone.js and webpy

This app provides functions for user management and login using backbone.js, webpy, and [python-social-auth](https://github.com/omab/python-social-auth). It is intended to work as a quickstart for other applications.

Started: 2012-09-23  
Last Update: 2014-08-16  
Author: cccarey  

## Setting up for Development

These notes leverage Apache as a web server and assume Apache and MySQL Server is installed and configured. If you would like to use a different web server, replace commands as necessary.

- Install PIP, build dependencies, create a python virtual environment, and activate it

        sudo apt-get install python-pip libmysqlclient-dev python-dev
        sudo pip install virtualenv
        virtualenv env
        source env/bin/activate

- Install python packages using pip

        pip install mysql-python web.py python-openid requests-oauthlib \
            python-social-auth sqlalchemy

- Enable proxy\_http module:

        sudo a2enmod proxy_http

- Add the reverse proxy config to apache (if you are going to use a different port, edit the file and change it in the appropriate places):

        sudo ln -s `pwd`/reverse_proxy.conf /etc/apache2/sites-enabled/b-w-openid-rev-proxy.conf

- Link web folder:

        cd web; sudo ln -s `pwd` /var/www/html/openid; cd ..

- Restart apache:

        sudo service apache2 restart

- Finally, create the shell script `services/setgoogleenv.sh` with your Google OAuth2 key and secret to start the webpy development server for services with the following contents. _Note the `PATH_PREFIX` variable inserted for the complete login path. See services/app/social_app.py for more information_:

        #!/usr/bin/env bash

        GOOGLE_OAUTH2_KEY="REPLACE_WITH_YOUR_KEY"
        GOOGLE_OAUTH2_SECRET="REPLACE_WITH_YOUR_SECRET"
        PATH_PREFIX="/backbone-webpy-openid-api"

        export GOOGLE_OAUTH2_KEY
        export GOOGLE_OAUTH2_SECRET
        export PATH_PREFIX

        ./code.py 8082

## Install/Setup

*Note:* these do not work with the default configuration of Apache on Ubuntu 14.04+. In addition, the environment variables for the Google OAuth2 key and secret will need to be incorporated into this setup. To be updated...

In order to setup the services as a wsgi app from within Apache, add the following.

- Install the following packages
    - python-mysqldb
    - python-webpy
    - python-openid
    - python-requests-oauthlib
    - python-sqlalchemy
    - libapache2-mod-wsgi

            sudo apt-get install python-mysqldb python-webpy \
            python-openid python-requests-oauthlib \
            python-sqlalchemy libapache2-mod-wsgi

- Set 'AllowOverride All' on the /var/www/ directory in /etc/apache2/sites-available/default
- Enable mod rewrite:

        sudo a2enmod rewrite

- Link services folder:

        cd services; sudo ln -s `pwd` /var/www/backbone-webpy-openid-api; cd ..

- Restart apache:

        sudo service apache2 restart

# Service API

### /info - GET

Provides basic application information. Sample:

        {
            "version": "v2014228", 
            "data": {
                "count": 0, 
                "google-oauth2_state": "Pqnj8dJKcdsw4BxS1RumaliKPkY36oCx", 
                "user_id": 3, 
                "social_auth_last_login_backend": "google-oauth2", 
                "ip": "127.0.0.1", 
                "session_id": "58c539a9e3a50d5d165139399f6dbea709943196", 
                "logged_in": true}
        }

### /user - GET

Returns information about the logged in user

        {
            "username": "christian.carey", 
            "first_name": "Christian", 
            "last_name": "Carey", 
            "nick_name": "Chris", 
            "email": "....", 
            "active": true, 
            "fullname": "Christian Carey", 
            "password": "", 
            "id": 3
        }

### /user - PUT

Saves user information. See `/user - GET` for request and response payload example.

### /logout - GET

Logs the user out of the application

> See [Python Social Auth documentation](http://psa.matiasaguirre.net/) for additional
> API calls.

# Other References

The sign-in buttons come from
[this project on GitHub](https://github.com/necolas/css3-social-signin-buttons).
