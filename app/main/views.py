from flask import render_template
from . import main


# your views go here i.e for home,about
@main.route("/")
def index():

    return render_template('index.html')


@main.route("/about")
def about():
    pass
