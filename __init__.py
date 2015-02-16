from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
from flask.ext.admin import Admin

app = Flask(__name__, static_url_path='')

#Add config file to the app
app.config.from_object('config')

#Adding the needed extensions
db = MongoEngine(app)
bcrypt = Bcrypt(app)
lm = LoginManager()
lm.init_app(app)
suser = Admin(app)

#Register blueprints
def register_blueprints(app):
    from ctfserver.views import users
    app.register_blueprint(users)

register_blueprints(app)

#Hack for getting login form everywhere
@app.context_processor
def login_form():
    from forms import LoginForm
    return dict(login_form=LoginForm())

#Admin views
from ctfserver.admin import run_admin
run_admin()

if __name__ == '__main__':
    app.run()
