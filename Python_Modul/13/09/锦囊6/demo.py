import csv

with open('./tmp/r1.csv') as f:
    # 创建reader对象
    reader = csv.reader(f)
    # 读取第一行数据
    h1 = next(reader)
    # 使用enumerate()函数获取表头及其索引
    for index, column in enumerate(h1):
        print(index, column)
