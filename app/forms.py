from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo
from .models import User


class SignUpForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(
                min=6, max=40, message='Field must be between 6 and 40 characters long.'
            ),
        ],
        render_kw={"id": "validationError"}
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(
                min=6, message='Minimum 6 characters.'
            ),
        ],
    )
    confirm = PasswordField(
        'Confirm password',
        validators=[
            DataRequired(),
            EqualTo(
                'password', message='Password is not match.'
            ),
        ],
    )
    submit = SubmitField("Register Now")

    def validate_username(self, username):
        existingUserUsername = User.query.filter_by(username=username.data).first()
        if existingUserUsername:
            raise ValidationError('That username already exist, please try again')


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()], render_kw={
                           "placeholder": "Username"})
    password = PasswordField("password", validators=[DataRequired()], render_kw={
                             "placeholder": "Password"})
    submit = SubmitField("Login")


class PostForm(FlaskForm):
    note = TextAreaField("Enter your note ...", validators=[DataRequired()])
    submit = SubmitField("Post")
