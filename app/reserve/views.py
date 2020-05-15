from . import reserve
from flask import render_template,flash, request, redirect, url_for
from flask_login import login_user, logout_user,login_required,current_user
from .forms import ReserveForm
from app.models import User,Order,Service
from app.main import main
from .. import db
@reserve.route('/reserve',methods = ["POST","GET"])
def reserve():
    form=ReserveForm()
    # new_reserve = Service.query.filter_by(name = reserve).first()
    if form.validate_on_submit:
        new_order = Order(user = current_user )
        db.session.add(new_order)
        db.session.commit()
        return  redirect(url_for('main.index'))
        
    flash("your table has been reserved,kindly check your email for more details")
        
                          
    return render_template('reserve.html',form=form)
