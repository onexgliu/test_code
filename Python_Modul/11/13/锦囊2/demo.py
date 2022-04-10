import shutil   # 导入高级文件操作模块
ff = input('请输入要判断的文件格式：')
for f in shutil.get_unpack_formats(): # 获取系统支持的解压缩格式
   if ff == f[0]:
       print(ff,'为系统支持的解压缩格式！')
       break  # 中止循环
