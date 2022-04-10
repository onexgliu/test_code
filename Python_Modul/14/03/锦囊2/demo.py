import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('原数据:', data)
print('转换为JSON格式字符串:', json.dumps(data))
print('转换为JSON格式字符串的长度:', len(json.dumps(data)))
print('去掉空格后的长度:', len(json.dumps(data, separators=(',', ':'))))
print('去掉空格后:', json.dumps(data, separators=(',', ':')))
