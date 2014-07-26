# backbone-webpy-openid

OpenID user and login control using Backbone.js and webpy

This app provides functions for user management and login using backbone.js,
webpy, and OpenID. It is intended to work as a quickstart for other
applications. In the future, it may be enhanced to also function as a plugin.

Started: 2012-09-23
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

        { "version": "v2013342" }

### /user - GET

Returns information about the logged in user

### /logout - GET

Logs the user out of the application

# Borrowed Code

OpenAuthID was borrowed from somewhere a few years ago and used in some
personal (and closed) projects. I believe, based on my delicious.com
bookmarks, it was borrowed from [Juan-Pablo Scaletti](http://jpscaletti.com),
but the link is no longer valid for me to verify.

The sign-in buttons come from
[this project on GitHub](https://github.com/necolas/css3-social-signin-buttons).
