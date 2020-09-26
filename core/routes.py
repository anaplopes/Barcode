# -*- coding: utf-8 -*-
from core.forms import ManyBarcodeForm, OneBarcodeForm
from core.services import BarcodeService
from flask import Blueprint, render_template, request, send_file


bp = Blueprint('barcode', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@bp.route('/barcode/many', methods=['GET', 'POST'])
def many_barcode():
    dirimage = 'core/code_image'
    zipname = 'core/codes.zip'
    form = ManyBarcodeForm()
    service = BarcodeService()
    del_zip = service.deleteZip(zipname=zipname)
    cls_dir = service.clearDir(dirname=dirimage)
    
    if request.method == 'POST' and form.validate_on_submit():
        file = request.files['file']
        codetype = request.form['codetype']
        includetext = True if request.form['includetext'] == 's' else False
        
        create_dirimage = service.createDir(dirname=dirimage)
        create_code = service.createManyImage(
            file=file,barcode_type=codetype, includetext=includetext, dirimage=dirimage)
        create_zip = service.createZipFile(zipname=zipname, dirimage=dirimage)
        return send_file(
            'codes.zip', mimetype='application/zip', attachment_filename='codes.zip', as_attachment=True)
    return render_template('many_barcode.html', form=form)


@bp.route('/barcode/one', methods=['GET', 'POST'])
def one_barcode():
    dirname = 'core/code_image'
    form = OneBarcodeForm()
    service = BarcodeService()
    
    if request.method == 'POST' and form.validate_on_submit():
        code = request.form['code']
        namefile = request.form['namefile']
        codetype = request.form['codetype']
        includetext = True if request.form['includetext'] == 's' else False
        
        create_dirimage = service.createDir(dirname=dirname)
        create_code = service.createOneImage(
            code=code, namefile=namefile, barcode_type=codetype, includetext=includetext, dirimage=dirname)
        return send_file(f'{dirname}/{namefile}.png', mimetype='image/png')
    return render_template('one_barcode.html', form=form)
