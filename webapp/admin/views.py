from flask import Blueprint, render_template, flash, redirect, url_for

from webapp.user.decorators import admin_required
from webapp.admin.forms import NewUnitForm
from webapp.main_page.models import Structure
from webapp.user.models import User
from webapp.database import db

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@admin_required
@blueprint.route('/')
def index():
    title = 'Редактор'
    return render_template('admin/index.html', page_title=title)


@admin_required
@blueprint.route('/new_unit', methods=['GET', 'POST'])
def new_unit():
    form = NewUnitForm()
    title = 'Редактор'
    if form.validate_on_submit():
        lead_user = User.query.filter_by(username=form.lead.data).first()
        if form.parent_id.data != '0':
            parent_unit = Structure.query.filter_by(name=form.parent_id.data).first()
            if parent_unit is not None:
                if lead_user:
                    unit = Structure(name=form.name.data, lead=lead_user.username, parent_id=parent_unit.id)
                    db.session.add(unit)
                    db.session.commit()
                    flash('Новое подразделение создано успешно')
                    return redirect(url_for('admin.new_unit'))
                else:
                    flash('Указанного пользователя для руководства не существует')
            else:
                flash('указано неверное родительское подразделение')
        else:
            if lead_user:
                unit = Structure(name=form.name.data, lead=lead_user.username)
                db.session.add(unit)
                db.session.commit()
                flash('Новое подразделение создано успешно')
                return redirect(url_for('admin.new_unit'))
            else:
                flash('Указанного пользователя для руководства не существует')
    return render_template('admin/new_unit.html', page_title=title, form=form)
