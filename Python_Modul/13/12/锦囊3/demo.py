import csv

# 以a+的方式打开文件表示追加
with open('./tmp/r1.csv', 'a+', newline='') as f:
    csv_write = csv.writer(f)
    a = ['7515131', '2019/6/12', '明日科技', '吉林省', '长春市', '3', '长春二道', '长春二道', '2019/6/15', '5']
    b = ['7515132', '2019/6/12', '明日科技', '吉林省', '四平市', '2', '长春二道', '长春二道', '2019/6/15', '6']
    csv_write.writerow(a)
    csv_write.writerow(b)
