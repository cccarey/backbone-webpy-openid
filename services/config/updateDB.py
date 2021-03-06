# -*- coding: UTF-8 -*-
import datetime

CURRENT_VERSION = 1

class UpdateDB:
    def __init__(self, db):
        self.db = db
        self.version = self.get_version()
        self.update_db()

    def get_version(self):
        try:
            result = self.db.query("select version from dbversion")
        except:
            return 0

        return result[0]["version"]

    def update_version(self, newVersion):
        oldVersion = newVersion - 1

        self.db.update('dbversion',
                version=newVersion,
                updated=datetime.datetime.now(),
                where='version = %s' % oldVersion
            )

        self.version = newVersion

    def update_db(self):
        while self.version < CURRENT_VERSION:
            if self.version < 1:
                '''
                Stores the version of the database. Specifically used for controlling versions
                '''
                self.db.query("""
                    create table dbversion (
                        `version` int not null default 0,
                        `updated` datetime not null
                    )
                    engine InnoDB;
                    """)
                self.db.insert('dbversion', version=1, updated=datetime.datetime.now())
                
                '''
                Users
                '''
                '''
                self.db.query("""
                    create table if not exists `users` (
                       `id` int not null auto_increment,
                        `user_login` varchar(255) not null,
                        `id_url` varchar(255),
                        `first_name` varchar(255),
                        `last_name` varchar(255),
                        `nick_name` varchar(50),
                        `is_admin` Boolean default false,
                        primary key(`id`)
                    )
                    engine InnoDB;
                    """)
                '''
                
                '''
                Session storage
                '''
                self.db.query("""
                    create table if not exists `sessions` (
                        `session_id` CHAR(128) UNIQUE NOT NULL,
                        `atime` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        `data` TEXT
                    )
                    engine InnoDB;
                    """)

                self.update_version(1)
                
