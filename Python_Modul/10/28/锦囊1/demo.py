import os.path  # 导入os.path模块

path = r'test.txt'  # 文件路径
stat1 = os.stat(path)  # 第一个stat元组
stat2 = os.stat(os.open(path, os.O_RDONLY))  # 第二个stat元组
print(os.path.samestat(stat1, stat2))  # 判断两个stat元组是否为同一个文件
stat3 = os.stat(os.open(r'temp.py', os.O_RDONLY))  # 第三个stat元组
print(os.path.samestat(stat1, stat3))  # 判断两个stat元组是否为同一个文件
