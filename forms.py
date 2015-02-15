from wtforms import Form, StringField, PasswordField, SubmitField, validators
from flask_wtf import RecaptchaField
from flask import request
from ctfserver.models import User

class RegistrationForm(Form):
    username = StringField('Username', [
                validators.Length(min=4, message="That's a very short team name you have"),
                ])
    email = StringField('Email ID', [
                validators.Length(min=6, max=35, message="That's a very short Email ID"),
                validators.Email(message="Invalid Email ID"),
                ])
    password = PasswordField('Password', [
                validators.Required(message="Please enter a password!"),
                validators.EqualTo('conf_password', message="Passwords mismatch!")
                ])
    conf_password = PasswordField('Confirm Password')
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.objects(username=self.username.data)
        if len(user) == 1:
            self.username.errors.append('A team has already registered with this name')
            return False

        em = User.objects(email=self.email.data)
        if len(em) == 1:
            self.email.errors.append('A team has already registered with this Email')
            return False

        ip = User.objects(host=request.remote_addr)
        if len(ip) == 1:
            self.username.errors.append('Someone has already registered using your IP address')
            return False

        return True

class LoginForm(Form):
    username = StringField('Username', [
                validators.Length(min=4),
                validators.Required()
                ])
    password = PasswordField('Password', [
                validators.Required()
                ])
    submit = SubmitField('Login')

class FlagSubmissionForm(Form):
    flag = StringField('Flag', [validators.Length(min=32, max=32)])
    submit = SubmitField('Pwn!')

