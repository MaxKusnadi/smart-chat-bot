from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class Command(Form):
    command = StringField('command', validators=[DataRequired()])
