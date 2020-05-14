import os

class Config:
  '''
  config class to be inheritted by other class
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://charlotte:new12@localhost/food'
  UPLOADED_PHOTOS_DEST ='app/static/photos'
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  SQLALCHEMY_TRACK_MODIFICATIONS=True
  MAIL_SERVER = 'smtp.gmail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    

class ProdConfig(Config):
  '''
  production config class
  '''
  # SQLALCHEMY_TRACK_MODIFICATIONS = False
  # SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")    

class DevConfig(Config):
  '''
  development config class
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://charlotte:new12@localhost/food'
  ##change the username to your username and password
  DEBUG = True


class TestConfig(Config):
  '''
  tests config class
  '''
  pass

config_options = {
  'development': DevConfig,
  'production': ProdConfig,
  'tests': TestConfig
}