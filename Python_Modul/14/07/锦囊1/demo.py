import json
with open('./tmp/mr1.json','w+') as f:
  f.write('[{"a": "A", "c": 3.0, "b": [2, 4]}]')
  f.flush()
  f.seek(0)
  print(json.load(f))
