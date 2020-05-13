from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_login import LoginManager



db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection ='strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)


def create_app(config_name):
    """
    creates an instances of the application 
    and passes the config name, i.e development
    or production, the will then pick the environments
    from the configuration classes in config
    """

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # set the configurations
    app.config.from_object(config_options[config_name])
    from .auth import auth as authentication_blueprint
    from .main import main as main_blueprint

    # configure UploadSet
    configure_uploads(app,photos)

    # initialiaze the database
    db.init_app(app)

    # register your blueprints here
    from app.main import main
    from app.auth import auth

    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(main_blueprint)

    login_manager.init_app(app)
    bootstrap.init_app(app)
    configure_uploads(app,photos)
    mail.init_app(app)

    return app
