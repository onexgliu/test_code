import json
data1 = [{ 'a':'MR-SOFT', 'b':(8, 88), 'c':8.8 ,'d':33}]
with open('aa.json', 'w') as f:
    json.dump(data1, f,allow_nan=False,sort_keys=True, indent=4)
