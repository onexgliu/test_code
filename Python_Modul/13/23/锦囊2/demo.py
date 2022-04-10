import csv
#定义excel类
class mri(csv.excel):
  delimiter = ';'
  dialect='excel'
csv.register_dialect('mri')  #注册csv方言mri
#写入文件
with open('./tmp/mrbooks.mri','w',newline='') as myFile:   #打开文件
    writer = csv.writer(myFile, mri)
    writer.writerow(['运单号','目的地'])
    writer.writerow(['0001', '长春'])
