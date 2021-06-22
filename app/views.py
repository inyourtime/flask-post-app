from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required
from .forms import LoginForm, PostForm
from .models import User, Post
from . import db

views = Blueprint('views', __name__, static_folder='static',
                  template_folder='templates')


@views.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('views.dashboard'))

    return render_template('home.html', form=form)


@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = PostForm()

    if form.validate_on_submit():
        username = current_user.username
        data = form.note.data
        user = User.query.filter_by(username=username).first()
        if user:
            new_post = Post(data=data, owner=user)
            try:
                db.session.add(new_post)
                db.session.commit()
                return redirect(url_for('views.dashboard'))
            except:
                return "error while add data"

    role = request.args.get('role')

    if role:
        notes = Post.query.filter_by(user_id=current_user.id).all()
        # print(notes)
        return render_template('dashboard.html', form=form, notes=notes)

    notes = Post.query.all()

    return render_template('dashboard.html', form=form, notes=notes)
