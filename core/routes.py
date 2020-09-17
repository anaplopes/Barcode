import treepoem
import pandas as pd
from core.forms import BarcodeForm
from flask import Blueprint, render_template, request, send_file


bp = Blueprint('barcode', __name__, url_prefix='/')

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = BarcodeForm()
    
    if request.method == 'POST' and form.validate():
        code = request.form['codetype']
        print(code)
        
        text = True if request.form['includetext'] == 'y' else False
        print(text)
        
        f = request.files['file']
        data = pd.read_csv(f, delimiter=';', encoding='utf-8')
        print(data)
        
        cont = 1
        for row in data:           
            image = treepoem.generate_barcode(barcode_type=code, data=row, options={"includetext": text})
            image.convert('1').save(f'core/image/{cont}.png')
            cont+=1
        
        return send_file('kit', mimetype='image/png')
    return render_template('index.html', form=form)
