import shutil  # 导入高级文件操作模块

shutil.copyfileobj(open('test.txt', 'r'), open('test1.txt', 'w'))  # 复制文件对象
