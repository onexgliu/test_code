import csv
import string
s1='{:0>10}'
formatter = string.Formatter()
with open('./tmp/r1.csv') as myFile:    #打开csv文件
     rows=csv.reader(myFile)            #读取csv文件
     for row in rows:                   #按行读取
         if rows.line_num == 1:         #忽略第一行表头
            continue
         print(formatter.format(s1,row[0])) #格式化“运单号”
