import csv

with open('./tmp/csv_test3.csv', 'w', newline='') as f:  # 如不指定newline='',会写入空行
    writer = csv.writer(f)
    writer.writerow(['订单编号', '会员名', '商品名称'])  # 写入一行标题
    writer.writerow(['mr00001', 'mrsoft', '零基础学Python'])  # 写入一行数据
    writer.writerow(['mr00002', 'mingri', 'Python从入门到项目实践'])  # 写入一行数据
    writer.writerow(['mr00003', 'mrkj', 'Python编程锦囊'])  # 写入一行数据
