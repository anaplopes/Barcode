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
        
        file = request.files['file']
        data = pd.read_csv(file, delimiter=';', encoding='utf-8')
        df = pd.DataFrame(data=data, columns= ['CODIGO','NM_ARQUIVO'])
        print(df)
        
        for index, row in df.iterrows():
            cod = str(row["CODIGO"])
            name = str(row["NM_ARQUIVO"])
            image = treepoem.generate_barcode(barcode_type=code, data=cod, options={"includetext": text})
            image.convert('1')
            image.save(f'core/uploads/{name}.png')
        
        return send_file('uploads', mimetype='image/png', as_attachment=True, attachment_filename='kit')
    return render_template('index.html', form=form)
