# backbone-webpy-openid

OpenID user and login control using Backbone.js and webpy

This app provides functions for user management and login using backbone.js,
webpy, and [python-social-auth](https://github.com/omab/python-social-auth).
It is intended to work as a quickstart for other applications.

Started: 2012-09-23  
Last Update: 2014-08-16  
Author.: cccarey  

## Install/Setup

Pre-requisites: apache2 and mysql-server installed - no further
apache2 mods

- Install the following packages:
    - python-mysqldb
    - python-webpy
    - python-openid
    - python-requests-oauthlib
    - python-sqlalchemy
    - libapache2-mod-wsgi

            sudo apt-get install python-mysqldb python-webpy \
            python-openid libapache2-mod-wsgi python-requests-oauthlib \
            python-sqlalchemy

- Set 'AllowOverride All' on the /var/www/ directory in /etc/apache2/sites-available/default
- Enable mod rewrite:

        sudo a2enmod rewrite

- Link services folder:

        cd services; sudo ln -s `pwd` /var/www/backbone-webpy-openid-api; cd ..

- Link web folder:

        cd web; sudo ln -s `pwd` /var/www/backbone-webpy-openid; cd ..

- Restart apache:

        sudo service apache2 restart

If you wish to run the internal webpy server to test changes for services, you
will need to enable a proxy or do something else to host the js on the same
domain/port. To enable proxy in apache with in conjunction with the instruct-
ions above, follow these steps:

- Enable proxy module and proxy\_http module:

        sudo a2enmod proxy\_http

- Add the following to the your apache config (/etc/apache2/sites-available/default)

        ProxyRequests Off
        <Proxy *>
                Order deny,allow
                allow from all
        </Proxy>
        <Location /backbone-webpy-openid-api/>
                ProxyPass http://localhost:8081/
                ProxyPassReverse http://localhost:8081/
                SetEnv force-proxy-request-1.0 1
                SetEnv proxy-nokeepalive 1
        </Location>

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
            "email": "christian.carey@gmail.com", 
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
