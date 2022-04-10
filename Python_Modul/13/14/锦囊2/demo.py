import csv
with open('./tmp/numMAC.csv') as myFile:   #打开csv文件
    data=csv.reader(myFile,delimiter=';')  #读取csv文件,设置分隔符为分号“;”
    for r in data:
       print(r)
