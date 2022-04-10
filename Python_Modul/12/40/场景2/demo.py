import sys      #  调入系统模块
import time     #  调入时间模块
sys.stdout.write('动态输出时间\n')
i=50
while i>0:
    sys.stdout.write("\r")
    sys.stdout.flush()
    sys.stdout.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime() ))
    time.sleep(0.5)
