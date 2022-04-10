import json

data1 = [{'a': 'MR-SOFT', 'b': (8, 88), 'c': 8.8, 'd': 33}]
print('正常：', json.dumps(data1, allow_nan=False, sort_keys=True))
print('缩进显示：', json.dumps(data1, allow_nan=False, sort_keys=True, indent=2))
