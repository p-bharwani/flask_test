from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'bby'}
    return render_template('index.html', title = 'Home', user = user)

# made using https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
