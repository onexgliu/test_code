import os.path                           # 导入os.path模块
path = r'E:/mr/test/pdf'  # 目录
filename = 'list.docx'  # 文件名
print(os.path.isfile(os.path.join(path,filename)))  # 判断是否为普通文件
