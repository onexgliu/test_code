import csv
csv.register_dialect('mr',delimiter='|',quoting=csv.QUOTE_NONE)
print(csv.list_dialects())
with open('./tmp/mrdata.mr',newline='') as f:
    reader=csv.reader(f,'mr')
    for row in reader:
        print(row)
