from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, ChangePassword


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'bensm'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    user = {'username': 'bensm'}
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', user=user, form=form)


@app.route('/history')
def history():
    user = {'username': 'bensm'}
    return render_template('history.html', title='History', user=user)


@app.route('/password', methods=['GET', 'POST'])
def password():
    user = {'username': 'bensm'}
    form = ChangePassword()
    if form.validate_on_submit():
        flash('Password changed successfully')
        return redirect('/index')
    return render_template(
        'password.html', user=user,
        title='Change Password', form=form)
