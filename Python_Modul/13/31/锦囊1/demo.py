import csv

with open('./tmp/csv_test.csv', 'w', newline='') as f:  # 指定newline=''，防止写入空行
    writer = csv.writer(f)
    writer.writerow(['订单编号', '会员名', '商品名称'])  # 写入一行表头
    data = [('mr00001', 'mrsoft', '零基础学Python'), ('mr00002', 'mingri', 'Python从入门到项目实践')
        , ('mr00003', 'mrkj', 'Python编程锦囊')]
    writer.writerows(data)  # 写入多行数据
