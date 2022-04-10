import csv
import pandas as pd

# 解决输出dataframe格式数据不对齐，显示不全的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# 读取csv文件数据
lines = list(csv.reader(open(r'./tmp/r1.csv')))
header, values = lines[0], lines[1:]
data1 = {h: v for h, v in zip(header, zip(*values))}
df = pd.DataFrame(data1)  # 转换成dataframe格式
print(df)
