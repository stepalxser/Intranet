import flask_wtf
import wtforms


class LoginForm(flask_wtf.FlaskForm):
    username = wtforms.StringField('Имя пользователя', validators=[wtforms.validators.DataRequired()], render_kw={'class': 'form-control'})
    password = wtforms.PasswordField('Пароль', validators=[wtforms.validators.DataRequired()], render_kw={'class': 'form-control'})
    submit = wtforms.SubmitField('Войти в интранет', render_kw={'class': 'btn btn-secondary'})
