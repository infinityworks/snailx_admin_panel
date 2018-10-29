from flask import render_template, Blueprint, redirect, url_for, flash, request
from forms.forms import AddSnailForm
from flask_login import current_user
from db.models import Trainer

add_snail_blueprint = Blueprint('add_snail', __name__)


@add_snail_blueprint.route("/snails/add", methods=["GET", "POST"])
def add_snail():
    if not current_user.is_authenticated:  # TODO: not
        return redirect(url_for('login.login'))

    trainer_model = Trainer()
    form = AddSnailForm()
    form.trainer_name.choices = [(str(t.id), t.name) for t in trainer_model.get_all_trainers()]

    if form.validate_on_submit():
        print(form.trainer_name.data)
        return 'validated'

    return render_template('add_snail.html', title='Add Snail', form=form)
