import json

with open('./tmp/77.json', 'a+') as f:  # 以追加方式打开文件
    f.seek(0)  # 默认偏移量在最后，调整到开头
    if f.read() == '':  # 判断是否为空，如果为空创建一个新字典
        data = {}
    else:
        f.seek(0)
        data = json.load(f)
    # 追加内容
    data['04'] = 'Python项目开发案例集锦'
    data['05'] = 'Python从入门到精通'
with open('./tmp/77.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False)
