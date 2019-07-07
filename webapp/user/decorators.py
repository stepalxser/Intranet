import functools

import flask
import flask_login


def admin_required(func):
    @functools.wraps(func)
    def decorated_view(*args, **kwargs):
        if flask.request.method in flask_login.config.EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif flask.current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not flask_login.current_user.is_authenticated:
            return flask.current_app.login_manager.unauthorized()
        elif not flask_login.current_user.is_admin:
            flask.flash('Эта страница доступна только админам')
            return flask.redirect(flask.url_for('index'))
        return func(*args, **kwargs)
    return decorated_view


def reset_required(func):
    @functools.wraps(func)
    def decorated_view(*args, **kwargs):
        if flask.request.method in flask_login.config.EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif flask.current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not flask_login.current_user.is_authenticated:
            return flask.current_app.login_manager.unauthorized()
        elif flask_login.current_user.need_reset:
            flask.flash('По соображениям безопасности, вам необходимо ввести новый пароль')
            flask_login.logout_user()
            return flask.redirect(flask.url_for('auth.reset_password'))
        return func(*args, **kwargs)
    return decorated_view
