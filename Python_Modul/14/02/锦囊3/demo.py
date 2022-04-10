import csv
import json
#读取csv文件
csvf=open('./tmp/mr2.csv','r')
reader=csv.DictReader(csvf)
#转换为json文件
with open('./tmp/mr2.json','w') as f:
  for r in reader:
    data=json.dump(r,f,ensure_ascii=False,indent=4)
    f.write(r'\n')

