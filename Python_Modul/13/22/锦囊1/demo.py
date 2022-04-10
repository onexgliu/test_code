import csv
csvFile = open('./tmp/csv_test5.csv', 'w',newline='')
fileheader = ['订单编号','会员名','商品名称']
dict_writer = csv.DictWriter(csvFile, fileheader)     #写入标题
dict_writer.writeheader()
dict_writer.writerow({'订单编号': 'mr00001', '会员名': 'mrsoft', '商品名称': '零基础学Python'})
csvFile.close()
