from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import logout_user

from webapp.user.decorators import admin_required
from webapp.user.forms import UploadAvatarForm, CropAvatarForm
from webapp.admin.forms import NewUnitForm, EditUnitForm, DeleteUnitForm, FiringUserForm
from webapp.main_page.models import Structure
from webapp.user.models import User
from webapp.database import db

from webapp.admin.utils import generate_random_password

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


@admin_required
@blueprint.route('/edit_unit', methods=['GET', 'POST'])
def edit_unit():
    form = EditUnitForm()
    title = 'Редактор'
    if form.validate_on_submit():
        unit = Structure.query.filter_by(name=form.name.data).first()
        if unit is not None:
            if form.new_name.data:
                unit.name = form.new_name.data
            if form.parent_id.data:
                parent_unit = Structure.query.filter_by(name=form.parent_id.data).first()
                unit.parent_id = parent_unit.id
            if form.lead.data:
                unit.lead = form.lead.data

            db.session.add(unit)
            db.session.commit()
            flash('Изменения внесены успешно')
            return render_template('admin/edit_unit.html', page_title=title, form=form)
        else:
            flash('Подразделение не существует')
            return render_template('admin/edit_unit.html', page_title=title, form=form)
    return render_template('admin/edit_unit.html', page_title=title, form=form)


@admin_required
@blueprint.route('/delete_unit', methods=['GET', 'POST'])
def delete_unit():
    form = DeleteUnitForm()
    title = 'Редактор'
    unit = Structure.query.filter_by(name=form.name.data).first()
    if form.validate_on_submit():
        if unit is not None:
            relative_units = Structure.query.filter_by(parent_id=unit.id).all()
            if relative_units is None:
                db.session.delete(unit)
                db.session.commit()
                flash('Подразделение удалено')
                return render_template('admin/delete_unit.html', page_title=title, form=form)
            else:
                units = [unit.name for unit in relative_units]
                units = ', '.join(units)
                flash(f'У подразделения есть зависимые отделы: {units}.')
                flash('Прежде чем его удалить необходимо перенести или растустить их')
                return render_template('admin/delete_unit.html', page_title=title, form=form)
        else:
            flash('Подразделение не существует')
            return render_template('admin/delete_unit.html', page_title=title, form=form)
    return render_template('admin/delete_unit.html', page_title=title, form=form)


@admin_required
@blueprint.route('/firing_user', methods=['GET', 'POST'])
def firing_user():
    form = FiringUserForm()
    title = 'Редактор'
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            flash('Такого пользователя не существует')
            return render_template('admin/firing_user.html', form=form, page_title=title)
        lead_units = Structure.query.filter_by(lead=user.username).all()
        if lead_units:
            lead_units = [unit.name for unit in lead_units]
            lead_units = ', '.join(lead_units)
            flash(f"Пользователь является руководителем для подразделений: {lead_units}.")
            flash('Прежде чем уволить сотрудника, необходимо передать руководство другим людям.')
            return render_template('admin/firing_user.html', form=form, page_title=title)

        user.info.work_unit = None
        user.actual = False
        user.password = generate_random_password()
        db.session.commit()

        flash('Пользователь уволен')
        return render_template('admin/firing_user.html', form=form, page_title=title)
    return render_template('admin/firing_user.html', form=form, page_title=title)


@admin_required
@blueprint.route('/edit_user')
def edit_user():
    title = 'Редактор'
    form_avatar = UploadAvatarForm()
    form_crop = CropAvatarForm
    return render_template('admin/edit_user.html')