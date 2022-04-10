import csv

with open('./tmp/r1.csv') as myFile:  # 打开csv文件
    rows = csv.reader(myFile)  # 读取csv文件
    mydata = list(rows)  # 转换成Python列表
    print(mydata[1][4])  # 输出特定行和列的数据
