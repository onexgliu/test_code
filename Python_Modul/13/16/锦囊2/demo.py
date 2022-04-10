import csv

with open('./tmp/b1.csv', newline='') as f:
    rows = csv.reader(f, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL, escapechar='%')  # 读取csv文件
    for row in rows:  # 按行读取
        print(','.join(row))
