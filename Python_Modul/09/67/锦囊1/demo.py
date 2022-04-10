import os  # 导入文件与操作系统相关模块

tuples = os.walk('f:/program/Python/Code/01')  # 遍历“f:/program/Python/Code/01”目录
for tuple1 in tuples:  # 通过for循环输出遍历结果
    print(tuple1, '\n')  # 输出每一级目录的元组
