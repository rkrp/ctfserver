from wtforms import Form, StringField, PasswordField, SubmitField, validators

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4)])
    email = StringField('Email ID', [validators.Length(min=6, max=35)])
    password = PasswordField('Password')
    conf_password = PasswordField('Confirm Password')
    submit = SubmitField()

class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4)])
    password = PasswordField('Password')
    submit = SubmitField('Login')

class FlagSubmissionForm(Form):
    flag = StringField('Flag', [validators.Length(min=32, max=32)])
    submit = SubmitField()

