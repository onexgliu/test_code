import sys

sys.stdout.write('请输入出发地点的横、纵坐标值:')  # 提示用户输入字符串
x, y = sys.stdin.readline().split(',')  # 一行输入两个不限定类型的值
sys.stdout.write('请输入你的姓名、年龄和身高：\n')  # 提示用户输入字符串
name, age, height = sys.stdin.readline().split(',')  # 一行输入3个不限定类型的值
a, b = map(int, sys.stdin.readline().split())  # 一行输入两个限定类型为int的值
print(x, y)
print(age)
print(a, b)

import sys

sum = 0
sys.stdout.write('请输入多位加数，中间用空格分开：')  # 提示用户输入
for x in sys.stdin.readline().split(' '):
    sum = sum + int(x)
print(sum)
