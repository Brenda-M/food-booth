from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

admin = Admin()
db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
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


    # initialiaze the database
    db.init_app(app)
    admin.init_app(app)

    # register your blueprints here
    from app.main import main
    from app.auth import auth
    from app.adm import adm
    from app.reserve import reserve

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(adm)
    app.register_blueprint(reserve)


    login_manager.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    configure_uploads(app,photos)
    mail.init_app(app)

    return app
