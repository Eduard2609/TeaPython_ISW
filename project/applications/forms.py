from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired



class SuggestionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired()])
    install_command = StringField('Install Command', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AdminForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired()])
    install_command = StringField('Install Command', validators=[DataRequired()])
    image_file = StringField('Image File', validators=[DataRequired()])
    submit = SubmitField('Submit')
