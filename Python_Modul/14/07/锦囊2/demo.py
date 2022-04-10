import json
with open('./tmp/mr1.txt','r') as f:
    data = json.load(f)
    for line in data:
        print(line['city'])
