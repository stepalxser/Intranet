from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


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
