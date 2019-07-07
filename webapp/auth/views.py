import flask
import flask_login

import webapp.auth.forms as forms
from webapp.user.models import User

blueprint = flask.Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/login')
def login():
    if flask_login.current_user.is_authenticated:
        return flask.redirect(flask.url_for('index'))
    title = 'Авторизация'

    login_form = forms.LoginForm()
    return flask.render_template('auth/login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = forms.LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.verify_password(form.password.data):
            flask_login.login_user(user, remember=True)
            return flask.redirect(flask.url_for('index'))
    flask.flash('Incorrect auth')
    return flask.redirect(flask.url_for('auth/login'))


@blueprint.route('/logout')
def logout():
    flask_login.logout_user()
    flask.flash('You are logout')
    return flask.redirect((flask.url_for('auth.login')))

