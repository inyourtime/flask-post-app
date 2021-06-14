from flask import Blueprint, render_template, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import SignUpForm, LoginForm
from . import db
from .models import User

auth = Blueprint('auth', __name__, static_folder='static', template_folder='templates')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = SignUpForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hashPassword = generate_password_hash(password)
        newUser = User(username=username, password=hashPassword)
        try:
            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for('views.home'))
        except:
            return 'Error while add user'
    
    return render_template('register.html', form=form)


@auth.route('/login', methods=['POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

    return "<h1>login</h1>"


@auth.route('/logout')
def logout():
    return "<h1>logout</h1>"
