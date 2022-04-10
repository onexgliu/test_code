import csv
with open('./tmp/mrdata1.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=' ',quotechar='|', quoting=csv.QUOTE_NONE,escapechar='-')
    writer.writerow(['编号','员工姓名', '卡号', '备注'])
    writer.writerow(['mr001', '高猿员', '6229 9999 123','mr'])
    writer.writerow(['mr002', '小李', '6222 8888 456','mr'])
