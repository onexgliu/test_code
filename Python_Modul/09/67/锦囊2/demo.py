import os  # 导入文件与操作系统相关模块

tuples = os.walk('f:/program/Python/Code/01')  # 遍历“f:/program/Python/Code/01”目录
for root, dirs, files in tuples:  # 通过for循环输出遍历结果
    print('文件目录：', root)  # 输出文件目录
    print('子目录：', dirs if dirs else '无')  # 输出子目录
    print('文件：', files if files else '无')  # 输出文件
