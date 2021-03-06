from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Address, Menu, Service, Order


#creating app instance
app = create_app('production')

manager = Manager(app) 
Migrate = Migrate(app, db)

manager.add_command('server', Server) 
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
  return dict(app = app, db = db, User=User, Menu=Menu)

if __name__ == '__main__':
  manager.run()