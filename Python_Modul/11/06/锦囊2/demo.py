import shutil  # 导入高级文件操作模块
import datetime  # 导入日期时间模块

st = datetime.datetime.now()  # 获取开始时间
print('通过copyfileobj()方法复制')
with open(r'H:/temp.rar', 'rb') as src:  # 打开源文件
    with open(r'H:/temp/temp.rar', 'wb') as dst:  # 创建目标文件
        shutil.copyfileobj(src, dst, 1024)  # 分段复制
et = datetime.datetime.now()  # 获取结束时间
print('复制完成。用时：', et - st)
st = datetime.datetime.now()  # 获取开始时间
print('通过copyfile()方法复制')
shutil.copyfile(r'H:/temp.rar', 'H:/temp/temp2.rar')
et = datetime.datetime.now()  # 获取结束时间
print('复制完成。用时：', et - st)
