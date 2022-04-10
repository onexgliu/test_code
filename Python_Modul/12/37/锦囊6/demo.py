import sys

sys.stdout.write('请输入字符串：')  # 提示用户输入字符串
str1 = sys.stdin.readline()  # 记录用户输入
str2 = input()
sys.stdout.write('str1长度：' + str(len(str1)) + '\n')  # 输出字符串长度
sys.stdout.write('str2长度：' + str(len(str2)))  # 输出字符串长度
