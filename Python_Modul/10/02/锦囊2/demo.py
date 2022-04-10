import os.path  # 操作路径的模块

filename = ''  # 保存文件名的变量
if os.path.supports_unicode_filenames:  # 判断是否支持Unicode文件名
    filename = r'座右铭.txt'
else:
    filename = r'mot.txt'
open(filename, 'w')  # 创建或打开文件
print('文件名为：', filename)  # 输出文件名
