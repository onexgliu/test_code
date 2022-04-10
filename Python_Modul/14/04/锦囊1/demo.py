import json
a1 = '{"a": 123, "b": 456, "c": "明日科技"}'
a2='"\\"mr\\bar"'
json_decode = json.JSONDecoder()
print(json_decode.decode(a1))
print(type(json_decode.decode(a1)))
print(json_decode.decode(a2))
print(type(json_decode.decode(a2)))
