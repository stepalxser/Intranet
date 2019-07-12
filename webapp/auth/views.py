import flask_login
from flask import Blueprint, render_template, redirect, url_for, flash

import webapp.auth.forms as forms
from webapp.user.models import User
from webapp.database import db


blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/login')
def login():
    if flask_login.current_user.is_authenticated:
        return redirect(url_for('main_page.index'))
    title = 'Авторизация'

    login_form = forms.LoginForm()
    return render_template('auth/login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = forms.LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.verify_password(form.password.data):
            flask_login.login_user(user, remember=True)
            return redirect(url_for('main_page.index'))
    flash('Incorrect auth')
    return redirect(url_for('auth.login'))


@blueprint.route('/logout')
def logout():
    flask_login.logout_user()
    flash('You are logout')
    return redirect((url_for('auth.login')))


@blueprint.route('/reset_password')
def reset_password():
    if flask_login.current_user.is_authenticated:
        return redirect(url_for('main_page.index'))
    title = 'Смена пароля'

    reset_password_form = forms.ResetPasswordForm()
    return render_template('auth/reset_password.html', page_title=title, form=reset_password_form)


@blueprint.route('/process-reset-password', methods=['POST'])
def process_reset_password():
    form = forms.ResetPasswordForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if not user:
            flash('Пользователя с такими логином не существует. Введите правильные данные.')
            return redirect(url_for('auth.reset_password'))
        if not user.verify_password(form.old_password.data):
            flash('Вы ввели старый пароль неправильно. Попробуйте снова')
            return redirect(url_for('auth.reset_password'))

    user.password = form.new_password1.data
    user.need_reset = False
    db.session.commit()

    flash('Смена пароля выполнена успешно. Попробуйте зайти с новым паролем.')
    return redirect(url_for('auth.login'))




