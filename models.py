import datetime
from flask import url_for
from ctfserver import db

class User(db.Document):
    #id = db.IntField(primary_key=True)
    username = db.StringField(min_length=4, max_length=32, required=True)
    password = db.StringField(min_length=60, max_length=60, required=True)
    email = db.EmailField()
    banned = db.BooleanField(default=False)

    host = db.StringField(required=True)
    services = db.ListField(db.EmbeddedDocumentField('Service'))

    def is_authenticated(self):
        return True

    def is_active(self):
        return not self.banned

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self._id)

    def auth_user(username, password):
        user = User.objects(username__exact=username)
        hash = user.password
        if bcrypt.check_password_hash(hash, password):
            return True
        else:
            return False

class Service(db.EmbeddedDocument):
    name = db.StringField(max_length=128, required=True)
    port = db.IntField(min_value=1, max_value=65535, required=True)
    is_running = db.BooleanField(default=False)
    point = db.IntField(default=0, min_value=0)


