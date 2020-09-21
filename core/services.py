# -*- coding: utf-8 -*-
import os
import zipfile
import treepoem
import pandas as pd


class BarcodeService():
    
    def deleteZip(self, filename):
        zipf = os.path.exists(filename)
        if zipf:
            os.remove(filename)
    
    def clearDir(self, dir):
        for root, dirs, files in os.walk(dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))

    def createImage(self, file, barcode_type, includetext):
        data = pd.read_csv(file, delimiter=';', encoding='utf-8')
        df = pd.DataFrame(data=data, columns= ['CODIGO','NM_ARQUIVO'])
        
        for index, row in df.iterrows():
            image = treepoem.generate_barcode(
                barcode_type=barcode_type,
                data=str(row["CODIGO"]),
                options={"includetext": includetext})
            image.convert('1').save(f'code/{str(row["NM_ARQUIVO"])}.png')

    def createZipFile(self, ziplocal, dirimage):
        zipf = zipfile.ZipFile(ziplocal,'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(dirimage):
            for file in files:
                zipf.write(f'{dirimage}{file}')
        zipf.close()
