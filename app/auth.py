from flask import Blueprint, render_template, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
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
        hash_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hash_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Now, you can login !', category='register_success')
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

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('views.dashboard'))
        
        flash('Invalid login, please try again !', category='invalid_login')
        return redirect(url_for('views.home'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successfully !', category='logout')
    return redirect(url_for('views.home'))
