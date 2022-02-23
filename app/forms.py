from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Email

class EmailPasswordForm(Form):
    username = TextAreaField('Username', validators = [DataRequired()])
    email = TextAreaField('Email', validators = [DataRequired(), Email])