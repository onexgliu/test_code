import json

with open('./tmp/city.json', 'r') as json_file:
    data = json_file.read()
    val = json.loads(data)
    print(type(val))
    print(val)
