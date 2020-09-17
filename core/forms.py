from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired

code_choice = [
    ('', '-- Select --'),
    ('qrcode', 'QR Code'),
    ('azteccode', 'Aztec Code'),
    ('pdf417', 'PDF417'),
    ('interleaved2of5', 'Interleaved 2 of 5'),
    ('code128', 'Code 128'),
    ('code39', 'Code 39'),
    ('ean13', 'Ean 13')
]

class BarcodeForm(FlaskForm):
    codetype = SelectField('Code Type', choices=code_choice, validators=[DataRequired()])
    file = FileField('File', validators=[FileRequired(), FileAllowed(['csv'], 'csv only!')])
    includetext = BooleanField('Include Text')
    submit = SubmitField('Generator')
