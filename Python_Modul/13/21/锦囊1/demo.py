import csv

with open('mrdata.csv', 'w', newline='') as csvfile:
    fieldnames = ['运单号', '目的地', '客户运费']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'运单号': '800123', '目的地': '长春', '客户运费': 4})
    writer.writerow({'运单号': '800124', '目的地': '吉林', '客户运费': 5})
    writer.writerow({'运单号': '800125', '目的地': '四平', '客户运费': 5})
