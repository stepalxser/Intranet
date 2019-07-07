from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Войти в интранет', render_kw={'class': 'btn btn-secondary'})


class ResetPasswordForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], render_kw={'class': 'form-control'})
    old_password = PasswordField('Старый пароль', validators=[DataRequired()], render_kw={'class': 'form-control'})
    new_password1 = PasswordField('Новый пароль', validators=[DataRequired()], render_kw={'class': 'form-control'})
    new_password2 = PasswordField('Повторите новый пароль', render_kw={'class': 'form-control'},
                                  validators=[DataRequired(), EqualTo('new_password1', 'Данные нового пароля должны совпадать')])
    submit = SubmitField('Подтвердить', render_kw={'class': 'btn btn-secondary'})
