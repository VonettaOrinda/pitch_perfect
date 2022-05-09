from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    title=StringField('Pitch_Title')
    category=SelectField('Pitch_Category')
    pitch=TextAreaField('Pitch')
    submit=SubmitField('Submit')
