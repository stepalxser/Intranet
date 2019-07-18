from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField
from flask_wtf.file import FileField, FileAllowed, FileRequired


class AvatarForm(FlaskForm):
    image = FileField('Upload (<=3M)', render_kw={'class': 'form-control-file'},
                      validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'The file format should be .jpg or .png.')])
    presubmit = SubmitField('Загрузить аватар',
                         render_kw={'class': 'btn btn-secondary', })
    x = HiddenField()
    y = HiddenField()
    w = HiddenField()
    h = HiddenField()
    submit = SubmitField('Сохранить', render_kw={'class': 'btn btn-secondary'})
