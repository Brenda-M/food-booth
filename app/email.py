from flask_mail import Message
<<<<<<< HEAD
from . import mail 
from flask import render_template

def mail_message(subject,template,to,**kwargs):
    sender_email = 'foodbooth4@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)
=======
from flask import render_template
from . import mail

def order_email(subject, template, to, **kwargs):
  sender_email = 'noreplaymail84@gmail.com'

  email = Message(subject, sender=sender_email, recipients=[to])
  email.body= render_template(template + ".txt",**kwargs)
  email.html = render_template(template + ".html",**kwargs)
  mail.send(email)
>>>>>>> 0a369e4... add cart
