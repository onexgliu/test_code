import string  # 导入字符串模块
cn = '没什么是你能做却办不到的事。'
en = "There's nothing you can do that can't be done."
result = string.capwords(en)   # 每个单词首字母转换为小写
print(cn)
print('转换前：',en)
print('转换后：',result)
