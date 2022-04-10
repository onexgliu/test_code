import string  # 导入字符串模块
s = "do not,for   one repulse,give   up the purpose that you resolved to effect."
result = string.capwords(s) # 以逗号为分隔符，将各子句的首字母转换为小写
print('转换前：',s)
print('转换后：',result)
