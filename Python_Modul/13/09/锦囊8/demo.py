import csv

header = True
# 打开文件
with open('./tmp/r1.csv', 'r') as f:
    reader = csv.reader(f)
    header = [r for r in reader]
    if len(header) == 0:
        header = False
        print('csv文件无表头!')
    else:
        header = True
        print('csv文件有表头!')
