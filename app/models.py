from . import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer ,primary_key = True)
	username = db.Column(db.String(255), index = True)
	email = db.Column(db.String(255),unique = True, index = True)
	pass_secure = db.Column(db.String(255))
	phone_number = db.Column(db.Integer)

	orders  = db.relationship('Order', backref = 'user' , lazy = 'dynamic')

	@property
	def password(self):
		raise AttributeError('You cannot read the password attribute')

	@password.setter
	def password(self, password):
		self.pass_secure = generate_password_hash(password)


	def verify_password(self,password):
		return check_password_hash(self.pass_secure,password)
	

			
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

		