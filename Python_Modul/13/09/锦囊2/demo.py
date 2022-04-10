import csv
with open('./tmp/r1.csv') as myFile:   #打开csv文件
     rows=csv.reader(myFile)            #读取csv文件
     for row in rows:                   #按行读取
         print(row[0])                  #第0列
