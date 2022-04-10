import csv
datas = [{'订单编号':'mr00001','会员名':'mrsoft'},{'订单编号':'mr00002','会员名':'mingri'},{'订单编号':'mr00003','会员名':'mrkj'}]
with open('./tmp/test_csv_data.csv', 'w', newline='') as f:
     writer = csv.DictWriter(f, ['订单编号', '会员名'])  #写入表头，第一行数据
     writer.writeheader()
     for row in datas:
        writer.writerow(row)
        #写入多行
        writer.writerows(datas)
