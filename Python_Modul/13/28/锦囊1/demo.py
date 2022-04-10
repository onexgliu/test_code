import csv
with open('./tmp/mrdata.csv')as csvfile:
  reader=csv.reader(csvfile)
  for row in reader:
         #忽略第1行
         if reader.line_num == 1:
            continue
         print(row)
