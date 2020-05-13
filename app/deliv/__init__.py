from flask import Blueprint

deliv = Blueprint('deliv', __name__)


from . import views