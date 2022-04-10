import os  # 文件与操作系统相关模块

print(os.popen(r'e:/mot.txt', 'r'))  # 采用系统默认的编辑器打开文本文件
print(os.popen(r'e:/qrcode.png', 'r'))  # 采用系统默认的编辑器打开图片文件
print(os.popen(r'e:/第1章  初识Python.docx', 'r'))  # 采用系统默认的编辑器打开Word文件
print(os.popen(r'e:/零基础学Python.pdf', 'r'))  # 采用系统默认的编辑器打开PDF文件
