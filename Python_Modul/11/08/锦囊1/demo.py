import shutil  # 导入高级文件操作模块

shutil.copystat('test.txt', 'test1.txt')  # 复制文件权限位、最后修改时间等信息
