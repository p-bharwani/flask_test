from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'bby'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in the Netherlands!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'Beauty and the Best was so awesome!'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)

# made using https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
