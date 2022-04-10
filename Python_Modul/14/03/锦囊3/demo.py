import json
a = dict(name='sandy', age=17,QQ='null')
print (a)
print (type(a))
b = json.dumps(a)
print (b)
print (type(b))
