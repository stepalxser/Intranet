from flask import Blueprint, render_template
from flask_login import login_required

from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/user')


@login_required
@blueprint.route('/<username>')
def user_page(username):
    user = User.query.filter_by(username=username).first_or_404()
    title = 'Страница пользователя'
    return render_template('user/user.html', page_title=title, user=user)
