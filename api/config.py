import logging
import os

from common.mongo_client import CustomMongoClient
from .routes import add_routes


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'uV9YVtL8gz2jgkLYFVMB/3zwxiqnE2Z5'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'api.log'
    LOGGING_LEVEL = logging.INFO
    MONGO_DEFAULT_DB_NAME = 'laputa'
    MONGO_PORT = 27017
    MONGO_URI = f'mongodb://localhost:{MONGO_PORT}'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'M7XQR644tbuqe6jgMnKGhOtoZLiiPBZz'


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SECRET_KEY = '2vH6O12xx4/BwVyDlepiGwB/iFZsFdNT'
    MONGO_DEFAULT_DB_NAME = 'test'


config = {
    "dev": "api.config.DevelopmentConfig",
    "test": "api.config.TestingConfig",
    "default": "api.config.BaseConfig"
}


def configure_app(app):
    # Retrieve config
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.cfg', silent=True)
    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    # Add routes
    add_routes(app)
    # Attach mongo client to the Flask application
    app.mongo_client = CustomMongoClient(app.config['MONGO_URI'],
                                         instance_db=app.config['MONGO_DEFAULT_DB_NAME'])
