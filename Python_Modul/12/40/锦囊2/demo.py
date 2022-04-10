import sys     # 调用sys模块
import time
sys.stdout.write('杀毒程序正在全盘检查，请稍后\n')
for i in range(20):
    sys.stdout.write("\r")
    if i%2==1 :
        sys.stdout.write("\\")
    else:
        sys.stdout.write("/")
    sys.stdout.flush()
    time.sleep(0.3)




import sys     # 调用sys模块
import time
sys.stdout.write("\n")
sys.stdout.write('计数程序\n')
i=0
while i<30:
    i=i+1
    sys.stdout.write("\r")
    sys.stdout.write(str(i))
    sys.stdout.flush()
    time.sleep(0.5)




import sys     # 调用sys模块
import time
sys.stdout.write("\n")
sys.stdout.write('倒数程序\n')
i=40
while i>0:
    i=i-1
    sys.stdout.write("\r")
    sys.stdout.write(str(i))
    sys.stdout.flush()
    time.sleep(1)
