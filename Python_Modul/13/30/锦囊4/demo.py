import csv
datas = [{'订单编号':'mr00001','会员名':'mrsoft'},{'订单编号':'mr00002','会员名':'mingri'},{'订单编号':'mr00003','会员名':'mrkj'}]
with open('./tmp/csv_test4.csv', 'w', newline='') as f:
     writer = csv.DictWriter(f, ['订单编号', '会员名']) #写入表头，第一行数据
     writer.writeheader()
     for row in datas:                                  #写入多行数据
        writer.writerow(row)
