from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, BooleanField
from wtforms.validators import DataRequired

from webapp.admin.utils import generate_random_password

class NewUnitForm(FlaskForm):
    name = StringField('Введите название подразделения', validators=[DataRequired()], render_kw={'class': 'form-control'})
    lead = StringField('Введите имя руководителя', validators=[DataRequired()], render_kw={'class': 'form-control'})
    parent_id = StringField('Введите название материнского подразделения(если его нет, то поставьте ноль)',
                            validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Создать подразделение', render_kw={'class': 'btn btn-secondary'})


class EditUnitForm(FlaskForm):
    name = StringField('Введите название подразделения', validators=[DataRequired()], render_kw={'class': 'form-control'})
    new_name = StringField('Введите новое название подразделения, если планируете его изменить', render_kw={'class': 'form-control'})
    lead = StringField('Введите название аккаунта нового руководителя, если планируете изменить', render_kw={'class': 'form-control'})
    parent_id = StringField('ВВедите новое материнское подразделние, если планируете изменить)', render_kw={'class': 'form-control'})
    submit = SubmitField('Внести изменения', render_kw={'class': 'btn btn-secondary'})


class DeleteUnitForm(FlaskForm):
    name = StringField('Введите название подразделения', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Распустить подразделение', render_kw={'class': 'btn btn-secondary'})


class FiringUserForm(FlaskForm):
    name = StringField('Введите логин пользователя', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Уволить сотрудника', render_kw={'class': 'btn btn-secondary'})


class AddUser(FlaskForm):
    username = StringField('Введите логин пользователя', validators=[DataRequired()], render_kw={'class': 'form-control'})
    first_name = StringField('Имя сотрудника', validators=[DataRequired()], render_kw={'class': 'form-control'})
    last_name = StringField('Фамилия', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = StringField('Пароль *', default=generate_random_password(), validators=[DataRequired()], render_kw={'class': 'form-control'})
    position = StringField('Должность сотрудника', validators=[DataRequired()], render_kw={'class': 'form-control'})
    work_unit = StringField('Название подразделения', validators=[DataRequired()], render_kw={'class': 'form-control'})
    email = StringField('Почта сотрудника', validators=[DataRequired()], render_kw={'class': 'form-control'})
    internal_phone = StringField('Внутренний телефон', validators=[DataRequired()], render_kw={'class': 'form-control'})
    mobil_phone = StringField('Мобильный телефон', validators=[DataRequired()], render_kw={'class': 'form-control'})
    corp_messenger = StringField('Аккаунт в корпоративном чате', validators=[DataRequired()], render_kw={'class': 'form-control'})
    office = StringField('Офис, в котором работает сотрудник', validators=[DataRequired()], render_kw={'class': 'form-control'})
    work_before = StringField('Компания в которой сотрудник работал ДО', validators=[DataRequired()], render_kw={'class': 'form-control'})
    first_day = DateField('Дата выхода на работу', validators=[DataRequired()],format='%d-%m-%Y',
                          render_kw={'class': 'form-control', "placeholder": "Укажите в формате 31-12-2009"})
    birthday = DateField('День рождения', validators=[DataRequired()], format='%d-%m',
                         render_kw={'class': 'form-control', "placeholder": "Укажите в формате 31-12"})
    submit = SubmitField('Добавить нового сотрудника', render_kw={'class': 'btn btn-secondary'})
    admin = BooleanField('Права администратора в интранете', default=False)

class EditUser(FlaskForm):
    pass
