from flask import render_template, Blueprint, redirect, url_for, flash, request
from forms.forms import LoginForm
from db.models import User, Snail
from flask_login import login_user, current_user, logout_user, login_required
from globals.globals import bcrypt, login_manager, db


login_blueprint = Blueprint('login', __name__)


@login_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index.index'))
    form = LoginForm()
    if form.validate_on_submit():
        users = User()
        user = users.get_user_by_username(form.username.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            #login_user(user, remember=True)
            return redirect(url_for('index.index'))
        else:
            flash('Login Unsuccessful. Invalid Credentials.', 'danger')
    return render_template('login.html', title='Login', form=form)