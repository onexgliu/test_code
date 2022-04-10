"""
功能：递归求数列
参数：n表示查看输出数列长度
"""


def recursion(n):
    if n <= 1:  # 判断长度小于等于1，即0和1的情况
        return n  # 直接返回n的值
    return recursion(n - 1) + recursion(n - 2)  # 递归，利用方程计算前两项相加之和


n = int(input("请输入要查看的数列长度:"))  # 用户输入查看数列长度
for i in range(0, n):  # 遍历
    print(recursion(i), end=' ')  # 输出数列值
