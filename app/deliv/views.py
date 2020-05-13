from . import deliv
from flask import render_template, url_for, redirect
from flask_login import login_required, current_user, login_user, logout_user
from app.models import Menu, Address, User
from .forms import Delivery
from app.email import order_email

@deliv.route('/menu')
def menu():
  
  menus = Menu.query.all()

  return render_template('deliv/menu.html', title = "Food gallery", items=menus)


@deliv.route('/delivery')
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

@deliv.route('/take_away')
def takeaway():
  users = User.query.all()
  for user in users:
    if user.email == current_user.email:
      order_email("Order Confirmation", "email/takeaway_order", user.email, user=user)
  flash('Your order has been received! You will receive a confirmation email shortly', 'success')

  return redirect(url_for('.main'))
  
  return render_template('delivery_info.html', title="Delivery Details", form=form)
