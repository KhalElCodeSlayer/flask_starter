import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER','./uploads')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://yourusername:yourpassword@localhost/databasename'
    SQLALCHEMY_TRACK_MODIFICATIONS = True # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    # conn = psycopg2.connect(SQLALCHEMY_DATABASE_URI, sslmode='require')

# class DevelopmentConfig(Config):
#     """Development Config that extends the Base Config Object"""
#     DEVELOPMENT = True
#     DEBUG = True

# class ProductionConfig(Config):
#     """Production Config that extends the Base Config Object"""
#     DEBUG = False