from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {} with remeber me {}'.format(
            form.username.data,
            form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)