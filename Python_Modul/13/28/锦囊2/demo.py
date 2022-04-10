import csv
with open('./tmp/mrdata.csv')as csvfile:
  reader=csv.reader(csvfile)
  for row in reader:
         print('行号：',reader.line_num)   #读取行号
