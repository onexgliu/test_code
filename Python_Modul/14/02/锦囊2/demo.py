import json
data1 = {
    "Title": "登录测试",
    "Input": {
      "username": "高猿员",
      "passwd": "111"
    }
}
with open('login.json', 'w') as f:
    json.dump(data1, f, indent=4,ensure_ascii=False)
