from flask_wtf import FlaskForm
from wtforms.fields import StringField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField,FileRequired,FileAllowed 

from flask.helpers import send_from_directory

class PropertyForm(FlaskForm):
    title =  StringField("Property Title", validators = [DataRequired()])
    description = TextAreaField("Description", validators = [DataRequired()])
    rooms = StringField("No. of Rooms", validators = [DataRequired()])
    bathrooms = StringField("No. of Bathrooms", validators = [DataRequired()])
    price = StringField("Price", validators = [DataRequired()])
    type = SelectField("Property Type", choices=[('House', 'House'), ('Apartment', 'Apartment')], validators = [DataRequired()]) 
    location = StringField("Location", validators = [DataRequired()])
    photo = FileField("Photo", validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'])])