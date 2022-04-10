import csv
class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '|'
with open('./tmp/mrdata.csv','r') as f:
   reader = csv.reader(f, dialect=my_dialect,quoting=csv.QUOTE_ALL)
   for row in reader:
      print(row)
