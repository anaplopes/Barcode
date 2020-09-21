# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
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
    file = FileField('Arquivo csv', validators=[FileRequired(), FileAllowed(['csv'], 'csv only!')])
    codetype = SelectField('Tipo de código', choices=code_choice, validators=[DataRequired()])
    includetext = SelectField('Incluir Texto', choices=[('s', 'Sim'), ('n', 'Não')], validators=[DataRequired()])
    submit = SubmitField('Gerar')
