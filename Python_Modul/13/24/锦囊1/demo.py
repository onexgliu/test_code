import csv


# 定义excel-tab类
class mytab(csv.excel_tab):
    dialect = 'excel-tab'


# 写入文件
with open('./tmp/mrsoft2.tsv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, mytab)
    spamwriter.writerow(['mrkj'] * 5 + ['www.mingrisoft.com'])
    spamwriter.writerow(['mrkj', '4006751066', '0431-84978981'])
# 读取文件
with open('./tmp/mrsoft2.tsv') as myFile:  # 打开csv文件
    rows = csv.reader(myFile)  # 读取csv文件
    for row in rows:  # 按行读取
        print(','.join(row))
