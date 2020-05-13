from app import create_app, db,admin
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User,Menu,Order,Service,MyModelView


#creating app instance
app = create_app('development')

manager = Manager(app) 
Migrate = Migrate(app, db)

manager.add_command('server', Server) 
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User)

if __name__ == '__main__':
  admin.add_view(MyModelView(User, db.session))
  admin.add_view(MyModelView(Menu, db.session))
  admin.add_view(MyModelView(Service, db.session))
  admin.add_view(MyModelView(Order, db.session))
  manager.run()