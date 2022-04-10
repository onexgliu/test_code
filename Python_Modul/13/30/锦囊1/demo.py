import csv

with open('./tmp/csv_test1.csv', 'w', newline='') as f:  # 如不指定newline='',有时会写入空行
    writer = csv.writer(f)
    writer.writerow(['订单编号', '会员名', '商品名称'])  # 写入一行标题
