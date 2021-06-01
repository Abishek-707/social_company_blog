from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from social_company_blog.models import User

class LoginForm(FlaskForm):
    email= StringField('email',validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField('Log In')

class RegistrationForm(FlaskForm):

    email= StringField('email',validators=[DataRequired(),Email()])
    username= StringField('username',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired(),EqualTo('confirm_pass',message='Password must match')])
    confirm_pass= PasswordField('confirm password', validators=[DataRequired()])
    submit=SubmitField('Register!')

    def validate_email(self,field):
        print(field)
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been already reagistered')


    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been already reagistered')


class UpdateUserForm(FlaskForm):

    email= StringField('email',validators=[DataRequired(),Email()])
    username= StringField('username',validators=[DataRequired()])
    picture= FileField('Update profile picture', validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Update')
        
