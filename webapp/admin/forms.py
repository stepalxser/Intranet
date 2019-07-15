from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class NewUnitForm(FlaskForm):
    name = StringField('Введите название подразделения', validators=[DataRequired()], render_kw={'class': 'form-control'})
    lead = StringField('Введите имя руководителя', validators=[DataRequired()], render_kw={'class': 'form-control'})
    parent_id = StringField('Введите название материнского подразделения(если его нет, то поставьте ноль)',
                            validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Создать подразделение', render_kw={'class': 'btn btn-secondary'})
