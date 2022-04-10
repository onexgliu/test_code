import os  # 文件与操作系统相关模块

filename = r'C:/cba.txt'  # 文件绝对路径
encodefn = os.fsencode(filename)  # 对路径进行编码
print('原路径：', filename)  # 输出原路径
print('编码后的类型：', type(encodefn))  # 输出编码后的类型
print('编码后的路径：', encodefn)  # 输出编码后的路径
decodefn = os.fsdecode(encodefn)  # 对编码后的路径进行解码
print('解码后的类型：', type(decodefn))  # 输出解码后的类型
print('解码后的路径：', decodefn)  # 输出解码后的路径
filename1 = r'cba.txt'  # 文件相对路径
encodefn = os.fsencode(filename1)  # 对路径进行编码
print('原路径：', filename1)  # 输出原路径
print('编码后的类型：', type(encodefn))  # 输出编码后的类型
print('编码后的路径：', encodefn)  # 输出编码后的路径
decodefn = os.fsdecode(encodefn)  # 对编码后的路径进行解码
print('解码后的类型：', type(decodefn))  # 输出解码后的类型
print('解码后的路径：', decodefn)  # 输出解码后的路径
