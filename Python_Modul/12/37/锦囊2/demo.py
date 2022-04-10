import sys

sys.stdout.write('请输入您的姓名：')  # 提示用户输入字符串
name = sys.stdin.readline().strip(' ')
sys.stdout.write('请输入您的年龄：')  # 提示用户输入字符串
age = sys.stdin.readline().lstrip(' ')
sys.stdout.write(name)  # 输出字符串
sys.stdout.write(age)  # 输出字符串
