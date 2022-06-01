from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from hello.models import User, Suggestion


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):  # un fel de throw error

        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already used. Please choose another one.')

    def validate_email(self, email):  # un fel de throw error

        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email already used. Please choose another one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):  # un fel de throw error
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already used. Please choose another one.')

    def validate_email(self, email):  # un fel de throw error
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('Email already used. Please choose another one.')


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