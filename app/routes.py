from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ahmed'}
    posts = [
        {
            'auther' : {'username': 'Another User'},
            'body' : 'What a beautiful day!'
        },
        {
            'auther' : {'username': 'Not ahmed'},
            'body': 'WOW, This post is posting'
        }

    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)