
from flask import Flask
from flask.ext.influxdb import InfluxDB
from config import config


# Extension initializations
db = InfluxDB()

def create_app(config_name):
    """Flask app factory"""
    app = Flask("spamapp")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Extension initializations
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

