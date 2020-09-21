# -*- coding: utf-8 -*-
from core.forms import BarcodeForm
from core.services import BarcodeService
from flask import Blueprint, render_template, request, send_file


bp = Blueprint('barcode', __name__, url_prefix='/')

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = BarcodeForm(request.form)
    service = BarcodeService()
    del_zip = service.deleteZip(filename='core/kit.zip')
    cls_dir = service.clearDir(dir='code/')
    
    if request.method == 'POST' and form.validate_on_submit():
        code = request.form['codetype']
        text = True if request.form['includetext'] == 's' else False
        file = request.files['file']
        create_code = service.createImage(file=file, barcode_type=code, includetext=text)
        create_zip = service.createZipFile(ziplocal='core/kit.zip', dirimage='code/')
        form.reset()
        return send_file('kit.zip', mimetype='application/zip', attachment_filename='kit.zip', as_attachment=True)
    return render_template('index.html', form=form)
