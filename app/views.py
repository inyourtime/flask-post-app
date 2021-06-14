from flask import Blueprint, render_template
from flask_login import current_user
from .forms import LoginForm

views = Blueprint('views', __name__, static_folder='static', template_folder='templates')


@views.route('/')
def home():
    form = LoginForm()
    return render_template('home.html', form=form, user=current_user)

