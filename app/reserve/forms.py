from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_login import current_user
from app.models import Address


class Delivery(FlaskForm):
  street_address = StringField('Address', validators=[DataRequired()])
  postal_code = StringField('Postal Address', validators=[DataRequired()])
  city = StringField('City', validators=[DataRequired()])
  submit = SubmitField('Post')