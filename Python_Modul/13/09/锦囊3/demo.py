import csv
with open('./tmp/r1.csv') as myFile:   #打开csv文件
     data=csv.reader(myFile)           #读取csv文件
     for i,rows in enumerate(data):    #按行读取
         if i==2:                      #如果行号为2，提取该行数据
             row=rows
             print(row)
