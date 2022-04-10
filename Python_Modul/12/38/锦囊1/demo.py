import sys
saveout = sys.stdout  # 在重定向前保存stdout
# 打开一个新文件用于写入。如果文件不存在，将会被创建。如果文件存在，将被覆盖
info = open('log.txt', 'w')
sys.stdout = info  # 所有后续的输出都会被重定向到刚才打开的新文件上
print('change stdout')  # 将输出结果“打印”到日志文件中，屏幕上不会看到输出
sys.stdout = saveout  # 重置stdout
info.close()  # 关闭日志文件
