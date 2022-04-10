import csv
import random
j=0
ID=0
csvname = input('请输入文件名:')
out = csv.writer(open('./tmp/'+csvname + '.csv','w', newline=''))
out.writerow(['ID', '学号', '班级'])         #写入表头
while j<5:
    for i in range(9):
      num=random.randint(20190000,20199999)  #随机生成“学号”
      Student=str(num)
      Grade='高一十二班'
      ID+=1
      out = csv.writer(open('./tmp/'+csvname + '.csv','a+', newline=''))
      out.writerow([ID,Student,Grade])        #写入学生数据
    j+=1
