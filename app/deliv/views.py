from . import deliv
from flask import render_template
from app.models import Menu

@deliv.route('/menu')
def main():
  
  menus = Menu.query.all()

  return render_template('menu.html', title = "Food gallery", items=menus)
