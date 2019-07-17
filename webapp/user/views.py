from flask import Blueprint, render_template, send_from_directory, request
from flask_login import login_required

from webapp.user.models import User, Structure
from webapp.main_page.models import Structure
from webapp.config import AVATARS_SAVE_PATH

blueprint = Blueprint('user', __name__, url_prefix='/user')


@login_required
@blueprint.route('/<username>')
def user_page(username):
    user = User.query.filter_by(username=username).first_or_404()
    user_unit = Structure.query.filter_by(id=user.info.work_unit).first()
    lead = User.query.filter_by(username=user_unit.lead).first()
    title = 'Страница пользователя'
    return render_template('user/user.html', page_title=title, user=user, lead=lead)


@login_required
@blueprint.route('/avatars/<path:filename>')
def get_avatar(filename):
    return send_from_directory(AVATARS_SAVE_PATH, filename)


@login_required
@blueprint.route('/upload_avatar', methods={'POST'})
def upload_avatar():
    f = request.files.get('file')
    raw_filename = avatars.save_avatar(f)
