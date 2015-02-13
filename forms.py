from wtforms import Form, StringField, PasswordField, validators
from ctfserver import bcrypt

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4)])
    email = StringField('Email ID', [validators.Length(min=6, max=35)])
    password = PasswordField('Password')

class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4)])
    password = PasswordField('Password')

class FlagSubmissionForm(Form):
    flag = StringField('Flag', [validators.Length(min=32, max=32)])

