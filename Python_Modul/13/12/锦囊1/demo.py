import csv
#写入数据
with open('./tmp/w1.csv', 'w', newline='') as f:
    csvw = csv.writer(f)
    csvw.writerow(['mrkj'] * 5 + ['www.mingrisoft.com'])
    csvw.writerow(['mrkj', '4006751066', '0431-84978981'])
#读取数据
with open('./tmp/w1.csv') as myFile:   #打开csv文件
     rows=csv.reader(myFile)            #读取csv文件
     for row in rows:                   #按行读取
         print(','.join(row))
