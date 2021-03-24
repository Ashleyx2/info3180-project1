from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    bedrooms = StringField('No. of Bedrooms', validators = [DataRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    property_type = SelectField(u'Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Photos only!')])