import os  # 文件与操作系统相关模块

filename1 = r'C:/cba.txt'  # 文件绝对路径
print('原路径：', filename1)  # 输出原路径
print('编码后：', os.fsencode(filename1))  # 输出编码后的路径
print('编码后的类型：', type(os.fsencode(filename1)))  # 输出编码后的路径类型
filename2 = 'cba.txt'  # 文件相对路径
print('原路径：', filename2)  # 输出原路径
print('编码后：', os.fsencode(filename2))  # 输出编码后的路径
print('编码后的类型：', type(os.fsencode(filename2)))  # 输出编码后的路径类型
