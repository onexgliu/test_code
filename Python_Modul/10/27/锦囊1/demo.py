import os.path  # 导入os.path模块

fp1 = open(r'test.txt', 'r').fileno()  # 第一个文件描述符对象
fp2 = os.open(r'test.txt', os.O_RDONLY)  # 第一个文件描述符对象
print(os.path.sameopenfile(fp1, fp2))  # 判断两个文件对象是否为同一个文件
