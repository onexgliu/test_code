import csv
import re

with open('./tmp/eat.csv', 'r') as f:
    reader = csv.DictReader(f)
    value = '麻辣烫'  # 关键字“麻辣烫”
    pattern = '.*' + value + '.*'  # 模糊匹配
    for row in reader:
        data = re.findall(pattern, row['商家名称'])  # 查询数据
        if len(data) > 0:
            print(row['序号'], row['商家名称'])
