import os  # 文件与操作系统相关模块
fileinfo = os.stat("mr.png")                          # 获取文件的基本信息
print("文件完整路径：", os.path.abspath("mr.png"))   # 获取文件的完整数路径
# 输出文件的基本信息
print("索引号：",fileinfo.st_ino)
print("设备名：",fileinfo.st_dev)
print("文件大小：",fileinfo.st_size," 字节")
print("最后一次访问时间：",fileinfo.st_atime)
print("最后一次修改时间：",fileinfo.st_mtime)
print("最后一次状态变化时间：",fileinfo.st_ctime)
