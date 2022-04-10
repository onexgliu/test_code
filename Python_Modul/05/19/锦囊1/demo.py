import random      # 导入随机数模块
number_list = [1,2,3,4,5]  # 数值列表
print('原列表顺序为：',number_list)
random.shuffle(number_list)  # 将列表元素随机排列
print('随机排列后的列表：',number_list)
