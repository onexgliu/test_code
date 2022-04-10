import random  # 导入随机数模块

random.seed()  # 默认种子
print('默认种子：', random.random())
random.seed()  # 默认种子2
print('默认种子2：', random.random())
random.seed(a=1)  # 整数种子
print('整数种子：', random.random())
random.seed(a=1)  # 整数种子2
print('整数种子2：', random.random())
random.seed(a='1', version=1)  # 字符种子
print('字符种子：', random.random())
random.seed(a='1', version=1)  # 字符种子2
print('字符种子2：', random.random())
