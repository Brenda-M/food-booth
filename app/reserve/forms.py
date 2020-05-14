from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField,StringField
from wtforms.validators import Required


class ReserveForm(FlaskForm):
    #   number=SelectField("number of people",choices=[("1" ,"1"),("2" ,"2") ,("3" ,"3")])
      number=StringField("type and submit anything to reserve a table")
      Submit=SubmitField("Submit")
      