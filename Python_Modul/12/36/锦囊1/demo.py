import sys

sys.stdout.write('用户输入：')
str = sys.stdin.read(5)  # 读取输入的前5个字符
sys.stdout.write(str)  # 输出字符串
