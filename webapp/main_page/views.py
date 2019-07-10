from flask import Blueprint, render_template
from flask_login import login_required

from webapp.user.decorators import reset_required
from webapp.main_page.models import Structure
from webapp.database import db


blueprint = Blueprint('main_page', __name__)


@blueprint.route('/')
@blueprint.route('/index')
@reset_required
def index():
    title = 'Главная'
    return render_template('main_page/index.html', page_title=title)


@login_required
@blueprint.route('/structure')
def structure():
    title = 'Организация'
    primary_units = db.session.query(Structure.id, Structure.name, Structure.parent_id).all()

    return render_template('main_page/structure.html', page_title=title, primary_units=primary_units)
