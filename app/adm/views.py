from . import adm
from .. import db,admin
from ..models import User,Menu,Order,Service,MyModelView



admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Menu, db.session))
admin.add_view(MyModelView(Service, db.session))
admin.add_view(MyModelView(Order, db.session))