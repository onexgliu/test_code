import json
data = [ { 'a':'mr', 'c':(66, 88), 'd':8.8,'b':'mrkj' } ]
print('原数据:', data)
print('JSON格式的字符串:', json.dumps(data))
print('排序后:', json.dumps(data, sort_keys=True))
