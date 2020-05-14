from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,FileField
from wtforms.validators import Required

class UpdateUser(FlaskForm):
  bio = TextAreaField('number of people needed per table.',validators = [Required()])
  submit = SubmitField('Submit')
class NewUser(FlaskForm):
  title = StringField("time of delivery", validators = [Required()])
  pitch = TextAreaField("Description", validators = [Required()])  
  category=SelectField("Category",
  choices=[("interview","interview"),("motivation","motivation"),("product","product"),("promotion","promotion")],validators = [Required()])
  submit=SubmitField("submit")
class CommentForm(FlaskForm):
  text = TextAreaField('Leave a feedback of our services:',validators=[Required()])
  submit=SubmitField('Submit')
class CommentForm(FlaskForm):
      text = TextAreaField('Leave a feedback of our services:',validators=[Required()])
  submit=SubmitField('Submit')
class CommentForm(FlaskForm):
      text = TextAreaField('Leave a feedback of our services:',validators=[Required()])
  submit=SubmitField('Submit')