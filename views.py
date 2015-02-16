from flask import Blueprint, request, redirect, render_template, url_for, flash
from flask.views import MethodView
from ctfserver import app
from ctfserver.models import *
from ctfserver.forms import *

users = Blueprint('users', __name__, template_folder='templates')

class ScoresView(MethodView):
    def get(self):
        users = User.get_scores()
        return render_template('scores/scores.html', users=users)

users.add_url_rule('/scores', view_func=ScoresView.as_view('scores'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    user = User()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        if user.auth_user(username, password):
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('users/login.html', form=form)

@app.route('/logout')
def logout():
    user = User()
    user.logout_user()
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.register_user(form.username.data, form.password.data, form.email.data, request.remote_addr)
        return redirect('/')
    else:
        return render_template('users/register.html', form=form)
