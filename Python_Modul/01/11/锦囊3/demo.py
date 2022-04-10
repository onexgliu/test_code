import string  # 导入字符串模块

cn = '不要只因一次失败，就放弃你原来决心想达到的目的。'
en = "do not,for one repulse,give up the purpose that you resolved to effect."
result = string.capwords(en, sep='o')  # 以o为分隔符
print(cn)
print('转换前：', en)
print('转换后：', result)
