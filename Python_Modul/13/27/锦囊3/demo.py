import csv

with open('./tmp/mrdata.csv') as f:
    reader = csv.DictReader(f)
    data = []
    # 获取csv文件的表头字段
    head = reader.fieldnames
    for row in reader:
        # 按表头信息提取第0列数据
        col1 = row[head[0]]
        # 将第0列数据转换成字符串保存到列表中
        data.append(''.join(col1))
print(data)
