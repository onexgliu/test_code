import os  # 文件与操作系统相关模块
print('路径是否存在：', os.access(r'test.txt', os.F_OK))  # 测试路径是否存在
print('路径是否可执行：', os.access(r'test.txt', os.X_OK))  # 测试路径是否可执行
print('路径是否可写：', os.access(r'test.txt', os.W_OK))  # 测试路径是否可写
print('路径是否可读：', os.access(r'test.txt', os.R_OK))  # 测试路径是否可读
