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


@login_required
@blueprint.route('/structure/<unit_id>')
def structure_init(unit_id):
    unit = Structure.query.filter_by(id=unit_id).first_or_404()
    subunits = Structure.query.filter_by(parent_id=unit.id).all()

    current_unit = Structure.query.filter_by(id=unit_id).first()
    unit_links = []
    while True:
        unit_links.append((current_unit.id, current_unit.name))
        if current_unit.parent_id != 0:
            current_unit = Structure.query.filter_by(id=current_unit.parent_id).first()
        else:
            unit_links.reverse()
            break

    return render_template('main_page/structure_unit.html', unit_id=unit, subunits=subunits, unit_links=unit_links)
