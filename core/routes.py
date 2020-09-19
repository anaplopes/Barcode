import os
import zipfile
import treepoem
import pandas as pd
from core.forms import BarcodeForm
from flask import Blueprint, render_template, request, send_file


bp = Blueprint('barcode', __name__, url_prefix='/')

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = BarcodeForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        code = request.form['codetype']
        print(code)
        
        text = True if request.form['includetext'] == 'y' else False
        print(text)
        
        file = request.files['file']
        data = pd.read_csv(file, delimiter=';', encoding='utf-8')
        df = pd.DataFrame(data=data, columns= ['CODIGO','NM_ARQUIVO'])
        print(df)
        
        for index, row in df.iterrows():
            image = treepoem.generate_barcode(barcode_type=code, data=str(row["CODIGO"]), options={"includetext": text})
            image.convert('1').save(f'core/download/{str(row["NM_ARQUIVO"])}.png')
            
        zipf = zipfile.ZipFile('core/kit.zip','w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk('core/download/'):
            for f in files:
                zipf.write(f'core/download/{f}')
        zipf.close()
        
        return send_file('kit.zip', mimetype = 'application/zip', attachment_filename= 'kit.zip', as_attachment = True)
    return render_template('index.html', form=form)
