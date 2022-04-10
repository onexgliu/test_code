import csv

with open('./tmp/r1.csv') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    print(rows[0])

import csv

with open('./tmp/r1.csv') as f:
    # 创建reader对象
    reader = csv.reader(f)
    # 读取第一行数据
    h1 = next(reader)
    print(h1)
