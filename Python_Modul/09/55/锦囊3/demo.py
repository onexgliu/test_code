import os  # 文件与操作系统相关模块
filelist = []  # 保存文本文件路径的列表
def getfilepath(path):
    for file in os.scandir(path):   # 遍历目录条目迭代器
        if file.is_dir():
            getfilepath(file)  # 递归调用获取遍历全部子目录
        elif file.is_file():
            if file.name.endswith('.txt'):  # 判断是否为文本文件
                filelist.append(file.path) # 将文件路径添加到列表
    return filelist  # 返回文本文件路径的列表
print(getfilepath(r'e:/mr/'))  # 调用函数
