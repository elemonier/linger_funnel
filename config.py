import os
basedir = os.path.abspath(os.path.dirname(__file__))

#This is the path of our database file.
SQLALCHEMY_DATABASE_URI = 'mysql://209.2.223.251/linger_api/'
#folder where we store the SQLAlchey-migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')