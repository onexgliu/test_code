import os  # 文件与操作系统相关模块

print('指定参数为空字典：', os.get_exec_path({}))  # 指定参数为空字典
print('不指定参数：', os.get_exec_path())  # 不指定参数
print('指定非空字典：', os.get_exec_path({'PATH': 'C:\Windows'}))  # 指定参数为非空字典
