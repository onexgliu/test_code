import os  # 文件与操作系统相关模块

for file in os.scandir(r'e:/mr/'):  # 遍历目录条目迭代器
    print(file.path)  # 输出完整的路径
