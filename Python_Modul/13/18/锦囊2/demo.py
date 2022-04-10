import csv
with open('./tmp/mrdata3.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='%',quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['编号','员工姓名', '卡号', '备注'])
    writer.writerow(['mr001', '高猿员', '62299999123','mr'])
    writer.writerow(['mr002', '小%李', '62228888456','mr'])
