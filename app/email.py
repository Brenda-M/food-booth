from flask_mail import Message
from . import mail 
from flask import render_template

def mail_message(subject,template,to,**kwargs):
    sender_email = 'noreplaymail84@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
from flask import render_template
from . import mail
>>>>>>> 3496579... add cart
=======
>>>>>>> fe7a7e4... update requirements file

def order_email(subject, template, to, **kwargs):
  sender_email = 'noreplaymail84@gmail.com'

  email = Message(subject, sender=sender_email, recipients=[to])
  email.body= render_template(template + ".txt",**kwargs)
  email.html = render_template(template + ".html",**kwargs)
  mail.send(email)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 0a369e4... add cart
>>>>>>> 3496579... add cart
=======
>>>>>>> fe7a7e4... update requirements file
