 
from . import deliv
from flask import render_template, url_for, redirect
from flask_login import login_required
from app.models import Menu, Address, User
from .forms import Delivery
from .email import order_email

@deliv.route('/menu')
def main():
  
  menus = Menu.query.all()

  return render_template('food.html', title = "Food gallery", items=menus)

@deliv.route('/reserve')
def deliv_info():

  form = reserve()

  if form.validate_on_submit():
    deliv_address = Address(phonenumber=current_user.phone_number, street_address=form.street_address.data, postal_code=form.postal_code.data, city=form.city.data)
    db.session.add(deliv_address)
    db.session.commit()

    current_user.phone_number = form.phone_number.data 

  users = User.query.all()
  for user in users:
      if user.email == current_user.email:
        delivery_email("Order Confirmation", "email/new_order", user.email, user=user)

        flash('Your table has been booked! You will receive a confirmation email shortly', 'success')
    
    return redirect(url_for('.main'))
  
  return render_template('display.html', title="reserve Details", form=form)