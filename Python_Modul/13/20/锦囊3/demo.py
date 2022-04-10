import csv

with open('./tmp/test_csv_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['订单编号'] == 'mr00001':
            print(row)
