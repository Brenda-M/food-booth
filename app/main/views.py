from flask import render_template,url_for
from . import main
from ..models import Service
from .. import db


# your views go here i.e for home,about
@main.route('/')
def index():
<<<<<<< HEAD
    services = Service
    return render_template('index.html', services = services)
    
=======

    return render_template('index.html')


>>>>>>> 859a5c0... add a cart remove item function
@main.route("/about")
def about():
    return render_template('about.html', about = about)
