from . import deliv
<<<<<<< HEAD
from app import db
from flask import render_template, url_for, redirect, request, flash
from flask_login import login_required, current_user, login_user, logout_user
from app.models import Menu, Address, User, Service, Order
from .forms import Delivery
from app.email import order_email
=======
from flask import render_template, url_for, redirect
from flask_login import login_required
from app.models import Menu, Address, User
from .forms import Delivery
from .email import order_email
>>>>>>> 3b0eb66... populate the form with the users phone number

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


@deliv.route('/delivery', methods=['GET', 'POST'])
def deliv_info():

  form = Delivery()

  if form.validate_on_submit():
    deliv_address = Address(phonenumber=current_user.phone_number, street_address=form.street_address.data, postal_code=form.postal_code.data, city=form.city.data)
    db.session.add(deliv_address)
    db.session.commit()

  current_user.phone_number = form.phone_number.data 

  users = User.query.all()
  for user in users:
    if user.email != current_user.email:
      order_email("Order Confirmation", "email/new_order", user.email, user=user)
      
    flash('Your order has been received! You will receive a confirmation email shortly', 'success')
  
    return redirect(url_for('.menu'))
  
  return render_template('deliv/delivery_info.html', title="Delivery Details", form=form)

