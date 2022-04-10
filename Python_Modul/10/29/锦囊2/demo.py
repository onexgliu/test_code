import os.path   # 导入os.path模块
wordpath = r'E:/mr/test/pdf/list.docx'  # Word文档的路径
folders = []
drive,path_and_file = os.path.splitdrive(wordpath) # 分割驱动器和目录
folders.append(drive[0])   # 获取驱动器中的盘符
path, file = os.path.split(path_and_file) # 分割路径和文件名
if path != '':  # 处理路径
    for i in path.split('/'):  # 将路径按/分隔
        if i != '':
            folders.append(i)
if file != '':   # 处理文件名
    folders.append(file)
print(folders)   # 输出分隔结果
