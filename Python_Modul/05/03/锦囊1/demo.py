import random  # 导入随机数模块

number_list = [1, 2, 3, 4, 5]  # 数值列表
str_tuple = ('1', '3', '5')  # 字符元组
print('列表随机元素为：', random.choice(number_list))
print('元组随机元素为：', random.choice(str_tuple))
