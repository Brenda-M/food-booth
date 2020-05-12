import os

class Config:
  '''
  config class to be inheritted by other class
  '''
  pass

class ProdConfig(Config):
  '''
  production config class
  '''
  pass

class DevConfig(Config):
  '''
  development config class
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/sendit'
  ##change the username to your username and password


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