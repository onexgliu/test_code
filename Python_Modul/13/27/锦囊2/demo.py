import csv
with open('./tmp/mrdata.csv')as csvfile:
  reader = csv.DictReader(csvfile)
  # 读取文件的表头字段信息
  head = reader.fieldnames
  for row in reader:
     # 按表头字段信息读取第0列数据
     col1 = row[head[0]]
     print(col1)
