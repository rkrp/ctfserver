from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager

#from ctfserver import models
#from ctfserver import views

app = Flask(__name__, static_url_path='')

#Add config file to the app
app.config.from_object('config')

app.config['MONGODB_SETTINGS'] = {'DB' : 'ctfdb'}
app.config['SECRET_KEY'] = 'Oooooh!S3cr3T!!!!'

db = MongoEngine(app)
bcrypt = Bcrypt(app)
lm = LoginManager()
lm.init_app(app)

def register_blueprints(app):
    from ctfserver.views import users
    app.register_blueprint(users)

register_blueprints(app)

#Hack for getting login form everywhere
@app.context_processor
def login_form():
    from forms import LoginForm
    return dict(login_form=LoginForm())

if __name__ == '__main__':
    app.run(debug=True)
