import sys  # 调入系统模块
import time  # 调入时间模块

batch = 1  # 控制安装的进度格
for i in range(int(100 / batch)):  # 100/batch 进度次数
    sys.stdout.write("\r")  # 回到行首
    sys.stdout.write('|' * i * batch + str(i * batch) + '%')  # 输出进度和百分比
    sys.stdout.flush()  # 刷新输出
    time.sleep(1)  # 1秒暂停再执行
