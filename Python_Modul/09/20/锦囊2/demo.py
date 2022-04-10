import os  # 文件与操作系统相关模块

project = input('请输入要执行的CMD命令(如osk、calc、eudcedit、mmc等)：')
try:
    os.startfile(project)  # 执行相应的CMD命令
except:
    print('不是有效的CMD命令！')
