import csv

dictreader = csv.DictReader(open('./tmp/test_csv_data.csv', newline=''), delimiter=',')
dictdata = {}  # 创建字典
i = 0
for row in dictreader:
    dictdata[i] = row  # 写入字典
    i = i + 1
print(dictdata)
