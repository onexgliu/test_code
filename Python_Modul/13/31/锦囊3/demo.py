import csv
data=[['西施','法师','2019.09.24'],['马超','战士','2019.08.15'],['曜','战士','2019.06.27']]
h=["新英雄","类别","上线时间"]
with open("./tmp/王者荣耀.csv",'w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(h)#写入表头
    writer.writerows(data)#写入数据
