from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy() #instance of the db

def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config_options[config_name])

  #intializing extensions
  db.init_app(app)
  

  #Registering blueprints
  from .main import main
  app.register_blueprint(main)

  from .auth import auth
  app.register_blueprint(auth)

  return app