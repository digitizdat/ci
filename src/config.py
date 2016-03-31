
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):

class TestingConfig(Config):


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
