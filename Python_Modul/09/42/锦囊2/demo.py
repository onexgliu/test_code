import os  # 文件与操作系统相关模块

info = os.lstat(r'E:/test.txt')  # 获取指定文件的信息
print('文件类型和权限：', info.st_mode)
print('inode编号：', info.st_ino)
print('文件的设备的ID：', info.st_dev)
print('硬链接数：', info.st_nlink)
print('所有者的用户ID：', info.st_uid)
print('所有者的组ID：', info.st_gid)
print('总大小：', info.st_size, '字节')
print('上次访问的时间：', info.st_atime)
print('上次修改的时间：', info.st_mtime)
print('上次状态更改的时间：', info.st_ctime)
