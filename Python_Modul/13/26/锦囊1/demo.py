import csv


# 定义excel类
class mydialect(csv.unix_dialect):
    dialect = 'unix'


# 写入文件
with open('./tmp/mrsoft2.usv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, mydialect)
    spamwriter.writerow(['mrkj'] * 5 + ['www.mingrisoft.com'])
    spamwriter.writerow(['mrkj', '4006751066', '0431-84978981'])
# 读取文件
with open('./tmp/mrsoft2.usv') as myFile:  # 打开文件
    rows = csv.reader(myFile)  # 读取文件
    for row in rows:  # 按行读取
        print(','.join(row))
