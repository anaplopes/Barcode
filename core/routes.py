# -*- coding: utf-8 -*-
from core.forms import BarcodeForm
from core.services import BarcodeService
from flask import Blueprint, render_template, request, send_file


bp = Blueprint('barcode', __name__, url_prefix='/')

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = BarcodeForm()
    service = BarcodeService()
    del_zip = service.deleteZip(zipname='core/codes.zip')
    cls_dir = service.clearDir(dirname='core/code_image')
    
    if request.method == 'POST' and form.validate_on_submit():
        code = request.form['codetype']
        text = True if request.form['includetext'] == 's' else False
        file = request.files['file']
        create_dirimage = service.createDir(dirname='core/code_image')
        create_code = service.createImage(file=file, barcode_type=code, includetext=text, dirimage='core/code_image')
        create_zip = service.createZipFile(ziplocal='core/codes.zip', dirimage='core/code_image')
        return send_file('codes.zip', mimetype='application/zip', attachment_filename='codes.zip', as_attachment=True)
    return render_template('index.html', form=form)
