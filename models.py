import datetime
from flask import url_for, session
from flask.ext.login import login_user, logout_user, current_user
from mongoengine import Q
from ctfserver import db, bcrypt, lm

#Callback for loading the user
@lm.user_loader
def load_user(userid):
    return User.objects(pk=userid)[0]

class User(db.Document):
    #id = db.IntField(primary_key=True)
    username = db.StringField(min_length=4, max_length=32, required=True, unique=True)
    password = db.StringField(min_length=60, max_length=60, required=True)
    email = db.EmailField(unique=True)
    banned = db.BooleanField(default=False)
    role = db.StringField(min_length=2, max_length=50, required=True)

    host = db.StringField(min_length=4, max_length=255, required=True, unique=True)
    points = db.IntField(default=0)
    services = db.ListField(db.EmbeddedDocumentField('Service'))

    def is_authenticated(self):
        return True

    def is_active(self):
        return not self.banned

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def auth_user(self, email, password):
        user = User.objects(Q(email=email) & Q(role='player')).first()
        if not user:
            return False

        hash = user.password
        if bcrypt.check_password_hash(hash, password):
            login_user(user)
            return True
        else:
            return False

    def register_user(self, username, password, email, host):
        user = User()
        user.username = username
        user.password = bcrypt.generate_password_hash(password)
        user.email = email
        user.host = host
        user.save()

    def logout_user(self):
        logout_user()

    @staticmethod
    def get_scores():
        users = User.objects(role='player').order_by('-points')

        rank = 1
        res = []
        for user in users:
            rec = {'rank' : rank,
                    'username' : user.username,
                    'points' : user.points,
                  }
            res.append(rec)
            rank += 1
        return res


class Service(db.EmbeddedDocument):
    name = db.StringField(max_length=128, required=True)
    port = db.IntField(min_value=1, max_value=65535, required=True)
    is_running = db.BooleanField(default=False)
    point = db.IntField(default=0, min_value=0)

