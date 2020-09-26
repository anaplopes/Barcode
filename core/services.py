# -*- coding: utf-8 -*-
import os
import zipfile
import treepoem
import pandas as pd


class BarcodeService():
    
    def deleteZip(self, zipname):
        zipf = os.path.exists(zipname)
        if zipf:
            os.remove(zipname)
    
    def clearDir(self, dirname):
        for root, dirs, files in os.walk(dirname, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
    
    def createDir(self, dirname):
        _dir = os.path.exists(dirname)
        if not _dir:
            os.mkdir(dirname)
            
    def createOneImage(self, code, namefile, barcode_type, includetext, dirimage):
        image = treepoem.generate_barcode(
            barcode_type=barcode_type, data=str(code), options={"includetext": includetext})
        image.convert('1').save(f'{dirimage}/{namefile}.png')

    def createManyImage(self, file, barcode_type, includetext, dirimage):
        data = pd.read_csv(file, delimiter=';', encoding='utf-8')
        df = pd.DataFrame(data=data, columns= ['CODIGO','NM_ARQUIVO'])
        
        for index, row in df.iterrows():
            image = treepoem.generate_barcode(
                barcode_type=barcode_type, data=str(row["CODIGO"]), options={"includetext": includetext})
            image.convert('1').save(f'{dirimage}/{str(row["NM_ARQUIVO"])}.png')

    def createZipFile(self, zipname, dirimage):
        zipf = zipfile.ZipFile(zipname,'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(dirimage):
            for file in files:
                zipf.write(f'{dirimage}/{file}')
        zipf.close()
