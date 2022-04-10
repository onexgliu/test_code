import json

with open('./tmp/city.json', 'r') as json_file:
    data = json_file.read()
    print(type(data))  # 输出类型
    result = json.loads(data)
    new_result = json.dumps(result, ensure_ascii=False)
    print(new_result)
