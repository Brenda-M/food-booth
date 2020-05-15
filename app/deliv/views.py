from . import deliv
from app import db
from flask import render_template, url_for, redirect, request, flash
from flask_login import login_required, current_user, login_user, logout_user
from app.models import Menu, Address, User, Service, Order
from .forms import Delivery
from app.email import order_email

@deliv.route('/menu')
def menu():
  
  menus = Menu.query.all()

  return render_template('deliv/menu.html', title = "Food gallery", items=menus)

@deliv.route('/menu', methods=['POST'])
def createOrder():
  cartItems = request.get_json()

  # get delivery service id
  delivery_service = db.session.query(Service).filter_by(name="delivery")
  delivery_id =  delivery_service.first().id

  orders = []

  # save order
  for item in cartItems:
    item_id = item.get(id)
    orders.append(Order(user_id=current_user.id, menu_id=item_id, service_id=delivery_id))

  db.session.add_all(orders)
  db.session.commit()

  menus = Menu.query.all()
  return render_template('deliv/menu.html', title = "Food gallery", items=menus)


@deliv.route('/delivery', methods=['POST', 'GET'])
def deliv_info():

  return render_template('deliv/delivery_info.html', title="Delivery Details", form=form)

