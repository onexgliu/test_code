import json

l = ['ID', [1, 2, 3], {'name': '明日科技'}]  # 创建一个列表
data = json.dumps(l, ensure_ascii=False)  # 将列表转换为JSON格式
print(repr(l))
print(data)  # 输出JSON格式
