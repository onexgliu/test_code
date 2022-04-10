import json

data = json.JSONEncoder(ensure_ascii=False).encode({'公司信息': ['明日科技', 'mrkj']})
print(type(data))
print(data)
