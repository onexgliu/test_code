import os  # 文件与操作系统相关模块

'''方法一'''
filelist = []
for file in os.scandir(r'e:/mr/'):  # 遍历目录条目迭代器
    if file.name.endswith('.txt'):
        filelist.append(file.path)
print(filelist)
'''方法二'''
filelist2 = [f.path for f in os.scandir(r'e:/mr/') if f.name.endswith('.txt')]
print(filelist2)
