import random      # 导入随机数模块
number_list = [1,2,3,4,5]          # 数值列表
str_tuple = ('6','7','8','9','0')  # 字符元组
print('随机抽取可变序列：',random.sample(number_list,3))
print('随机抽取不可变序列：',random.sample(str_tuple,3))
