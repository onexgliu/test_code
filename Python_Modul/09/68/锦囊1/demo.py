import os  # 文件与操作系统相关模块

fd = os.open(r'mot_en.txt', os.O_RDWR)  # 打开文件描述符
os.write(fd,
         'Our destiny offers not the cup of despair , but the chalice of opportunity.'.encode())  # 向文件中写入英文，将替换原文件中部分内容
os.close(fd)  # 关闭文件描述符
