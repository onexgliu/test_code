import string

s = string.Template('本书作者 $name, 创作时间 $time')  # 使用Template类构造函数
print(s.template)
