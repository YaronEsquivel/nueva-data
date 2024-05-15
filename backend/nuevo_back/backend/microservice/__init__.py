import os
from flask import Flask
# from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import config_dotenv

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    config_dotenv()
    
    app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('SQLALCHEMY_DATABASE_URI')
    # CORS(app)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    db.init_app(app)

    with app.app_context():
        from .controllers import user_controller_blueprint
        app.register_blueprint(user_controller_blueprint)
        return app