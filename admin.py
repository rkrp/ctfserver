from ctfserver import suser
from ctfserver.models import *
from flask.ext.admin.contrib.mongoengine import ModelView

def run_admin():
    suser.add_view(UserView(User))

class UserView(ModelView):
    column_filters = ['username']
    column_searchable_list = ('username', 'email')

