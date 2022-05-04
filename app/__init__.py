from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy




# Initializing Flask Extensions
bootstrap = Bootstrap()
db =SQLAlchemy()


def create_app(config_name):
# Initializing application
    app = Flask(__name__)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

#Setting up configuration
#creating the aoo configurations
    app.config.from_object(config_options[config_name])
    

    #initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # setting config
    from .request import configure_request
    configure_request(app)

    #will add the views and forms
    return app

