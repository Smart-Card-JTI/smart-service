from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    migrate = Migrate(app,db)
    
    from app.model import kantung_parkir,data_kartu

    from .controller import controller as ctrl_blueprint
    app.register_blueprint(ctrl_blueprint,url_prefix='/api/v1')
    app.app_context().push()


    return app