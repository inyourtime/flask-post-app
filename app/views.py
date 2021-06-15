from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from .forms import LoginForm

views = Blueprint('views', __name__, static_folder='static', template_folder='templates')


@views.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('views.dashboard'))

    return render_template('home.html', form=form)


@views.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
