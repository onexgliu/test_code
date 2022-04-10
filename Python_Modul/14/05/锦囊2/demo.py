import requests,json
try:
  #错误的网址
  url = 'https://www.ele.me/place/wzc1w5gjtp52?latitude=43.879003&longitude=125.424261'
  file = requests.get(url,timeout=3)
  list1 = json.loads(file.text)
  file1 = open('好吃的.txt','a')
  for l in list1:
    print(l['name'])
    file1.write(l['name']+'\n')
  file1.close()
except json.JSONDecodeError:
  print('获取数据失败！')
