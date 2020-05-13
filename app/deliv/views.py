from . import deliv
from flask import render_template, url_for
from flask_login import login_required
from app.models import Menu, Address, User
from .forms import Delivery

@deliv.route('/menu')
def main():
  
  menus = Menu.query.all()

  return render_template('menu.html', title = "Food gallery", items=menus)

@deliv.route('/delivery')
def deliv_info():

  form = Delivery()

  if form.validate_on_submit():
    deliv_address = Address(phonenumber=current_user.phone_number, street_address=form.street_address.data, postal_code=form.postal_code.data, city=form.city.data)
    db.session.add(deliv_address)
    db.session.commit()

  users = User.query.all()
    for user in users:
      if user.email == current_user.email:
        delivery_email("Order Confirmation", "email/new_order", user.email, user=user)

        flash('Your order has been received! You will receive a confirmation email shortly', 'success')

        