import os  # 文件与操作系统相关模块
root = r'E:/mr'
path = os.listdir(root)  # 获取指定路径下的目录和文件列表
list_dir = []   # 路径列表
for item in path: # 遍历获取到的目录和文件列表
    p = os.path.join(root,item)  # 连接目录
    if os.path.isdir(p):   # 判断是否为目录
        list_dir.append(p)
print('目录：',list_dir) # 输出目录列表
