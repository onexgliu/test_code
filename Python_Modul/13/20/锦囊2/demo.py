import csv

with open('./tmp/test_csv_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['订单编号'], row['会员名'])
