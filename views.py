from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from ctfserver.models import User, Service

users = Blueprint('users', __name__, template_folder='templates')

class ListView(MethodView):
    def get(self):
        users = User.objects.all()
        return render_template('users/scorecard.html', users=users)

users.add_url_rule('/scores', view_func=ListView.as_view('list'))

