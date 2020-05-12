from app import create_app, db
from flask_script import Manager,Server


#creating app instance
app = create_app('development')

manager = Manager(app) 
Migrate = Migrate(app, db)

manager.add_command('server', Server) 
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()