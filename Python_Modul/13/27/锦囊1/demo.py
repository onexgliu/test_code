import csv
with open('./tmp/mrdata.csv')as csvfile:
  reader = csv.DictReader(csvfile)
  head = reader.fieldnames
  print(head)
