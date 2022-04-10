import os  # 文件与操作系统相关模块
def formatTime(longtime):
    '''格式化日期时间的函数
       longtime：要格式化的时间
    '''
    import time                                   # 导入时间模块
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(longtime))
def formatByte(number):
    '''格式化文件大小的函数
       number：要格式化的字节数
    '''
    for (scale,label) in [(1024*1024*1024,"GB"),(1024*1024,"MB"),(1024,"KB")]:
        if number>= scale:                        # 如果文件大小大于等于1KB
            return "%.2f %s" %(number*1.0/scale,label)
        elif number == 1:                          # 如果文件大小为1字节
            return "1 字节"
        else:                                       # 处理小于1KB的情况
            byte = "%.2f" % (number or 0)
    # 去掉结尾的.00，并且加上单位“字节”
    return (byte[:-3] if byte.endswith('.00') else byte)+" 字节"
info = os.lstat(r'E:/test.txt')  # 获取指定文件的信息
print('文件类型和权限：',info.st_mode)
print('inode编号：',info.st_ino)
print('文件的设备的ID：',info.st_dev)
print('硬链接数：',info.st_nlink)
print('所有者的用户ID：',info.st_uid)
print('所有者的组ID：',info.st_gid)
print('总大小：',formatByte(info.st_size))
print('上次访问的时间：',formatTime(info.st_atime))
print('上次修改的时间：',formatTime(info.st_mtime))
print('上次状态更改的时间：',formatTime(info.st_ctime))
