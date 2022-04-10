import shutil  # 导入高级文件操作模块


def formatByte(number):
    '''格式化文件大小的函数
       number：要格式化的字节数
    '''
    for (scale, label) in [(1024 * 1024 * 1024, 'GB'), (1024 * 1024, 'MB'), (1024, 'KB')]:
        if number >= scale:  # 如果文件大小大于等于1KB
            return '%.2f %s' % (number * 1.0 / scale, label)
        elif number == 1:  # 如果文件大小为1字节
            return '1 字节'
        else:  # 处理小于1KB的情况
            byte = '%.2f' % (number or 0)
    # 去掉结尾的.00，并且加上单位“字节”
    return (byte[:-3] if byte.endswith('.00') else byte) + ' 字节'


result = shutil.disk_usage(r'E:\mr\test\pdf')  # 获取E盘的使用情况
print('总空间：', formatByte(result.total))
print('已用空间：', formatByte(result.used))
print('空闲空间：', formatByte(result.free))
