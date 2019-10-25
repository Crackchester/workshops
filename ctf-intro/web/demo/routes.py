from flask import render_template, flash, redirect, request
from flask_login import login_required, current_user, logout_user
from demo import app
from demo.login_form import LoginForm
from demo.models import login_user_with_form

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html.j2')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    if form.validate_on_submit():
        if login_user_with_form(form):
            return redirect('/index')

    return render_template('login.html.j2', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')
