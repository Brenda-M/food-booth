from . import adm
from .. import db,admin
from ..models import User,Menu,Order,Service,MyModelView
from app.auth.forms import RegForm,LoginForm
from app.auth import auth
from flask import render_template,flash, request, redirect, url_for



admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Menu, db.session))
admin.add_view(MyModelView(Service, db.session))
admin.add_view(MyModelView(Order, db.session))


@adm.route('/admin_signup',methods = ["POST","GET"])
def admin_signup():
    form = RegForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email = form.email.data, password=form.password.data ,is_admin =True)
        user.save()
        # mail_message("Welcome to Food-Booth","email/welcome",user.email,user=user)
        flash('Admin account created successfully')
        return  redirect(url_for('auth.login'))
    return render_template('admin_signup.html',registration_form=form )