import json

with open('./tmp/book1.json', 'r') as f1:
    mydict = json.load(f1)
    mydict['01'] = '零基础学Python'
with open('./tmp/book1.json', 'w') as f2:
    json.dump(mydict, f2, ensure_ascii=False)
