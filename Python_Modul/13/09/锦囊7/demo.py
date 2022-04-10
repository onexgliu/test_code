import csv

with open('./tmp/mrbook1.csv') as f:
    # 读取数据
    reader = csv.reader(f)
    h1 = next(reader)
    myval = []
    for row in reader:
        # 将“销量”列保存到myval列表中
        myval.append(int(row[4]))
    print(myval)
    print('当日最高销量：' + str(max(myval)) + '本')
