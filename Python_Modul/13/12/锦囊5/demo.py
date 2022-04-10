import csv
import pandas as pd

# 读取csv文件数据
lines = list(csv.reader(open(r'./tmp/r1.csv')))
header, values = lines[0], lines[1:]
data1 = {h: v for h, v in zip(header, zip(*values))}
df = pd.DataFrame(data1)  # 转换成dataframe格式
# 使用csv.writer()方法将dataframe格式数据写入csv文件
rows = df.values
with open('./tmp/r1副本.csv', 'w+', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(df.columns)
    for row in rows:
        writer.writerow(row)
