from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UploadAvatarForm(FlaskForm):
    image = FileField('Upload (<=3M)',
                      validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'The file format should be .jpg or .png.')])
    submit = SubmitField()
