import os  # 文件与操作系统相关模块

mask = 0o777  # 要设置的权限为八进制数777
previous = os.umask(mask)  # 设置为所有权限
print('原来的权限：', previous)  # 输出原来的权限
print('现在的权限：', mask)  # 输出现在的权限
