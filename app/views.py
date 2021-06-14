from flask import Blueprint, render_template
from .forms import LoginForm

views = Blueprint('views', __name__, static_folder='static', template_folder='templates')


@views.route('/')
def home():
    form = LoginForm()
    return render_template('home.html', form=form)


@views.route('/dashboard')
def dashboard():
    return '<h1>Dashboard</h1>'
