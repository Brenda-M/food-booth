from . import db,login_manager
from flask_login import current_user, UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_admin.contrib.sqla import ModelView

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(UserMixin,db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer ,primary_key = True)
	username = db.Column(db.String(255), index = True)
	email = db.Column(db.String(255),unique = True, index = True)
	pass_secure = db.Column(db.String(255))
	phone_number = db.Column(db.Integer)
	is_admin = db.Column(db.Boolean,default=False)

	orders  = db.relationship('Order', backref = 'user' , lazy = 'dynamic')

	@property
	def password(self):
		raise AttributeError('You cannot read the password attribute')

	@password.setter
	def password(self, password):
		self.pass_secure = generate_password_hash(password)


	def verify_password(self,password):
		return check_password_hash(self.pass_secure,password)

	def save(self):
		db.session.add(self)
		db.session.commit()
	
	def __repr__(self):
		return f'User {self.username}'
			
class Address(db.Model):
	id = db.Column(db.Integer, primary_key = True) 
	city = db.Column(db.String(20), nullable=False)
	street_address = db.Column(db.String(20), nullable=False)
	postal_code = db.Column(db.String(20), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Menu(db.Model):
	__tablename__ = 'menus'

	id = db.Column(db.Integer ,primary_key = True)
	name = db.Column(db.String(255), index = True)
	description =  db.Column(db.String(255), index = True)
	price = db.Column(db.Integer)
	orders  = db.relationship('Order', backref = 'menu' , lazy = 'dynamic')


class Service(db.Model):
	
	__tablename__ = 'services'

	id = db.Column(db.Integer ,primary_key = True)
	name =  db.Column(db.String(255), index = True)
	price = db.Column(db.Integer)
	orders  = db.relationship('Order', backref = 'service' , lazy = 'dynamic')
    

class Order(db.Model):
	__tablename__ = 'orders'

	id = db.Column(db.Integer ,primary_key = True)
	user_id =  db.Column(db.Integer, db.ForeignKey('users.id'))
	menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'))
	service_id =  db.Column(db.Integer, db.ForeignKey('services.id'))

class MyModelView(ModelView):
	def is_accessible(self):
		if current_user.is_admin:
			return current_user.is_authenticated
		else:
			return False

			
	def not_auth(self):
		return 'You are not authorized to the admin dashboard'

	def requestOrder(user, item, service):
		placeOrder = Order(user=user_id, service=service_id, item=menu_id)
		db.session.add(placedOrder)
		db.session.commit()

