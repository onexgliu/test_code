import csv

# 写入数据
with open('./tmp/b1.csv', 'w', newline='') as csvfile:
    w = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_NONE, escapechar='$'
                   , quotechar='|', skipinitialspace=False)
    w.writerow(['mrkj'] * 5 + ['www.mingrisoft.com'])
    w.writerow(['mrkj', 4006751066, 84978981])
# 读取数据
with open('./tmp/b1.csv', 'r') as f:
    reader = csv.reader(f)
    print(reader.__next__())
