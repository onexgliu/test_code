n = int(input("请输入一个数字："))  # 输入一个数字
for i in range(0, n):  # 使用for循环进行穷举
    for j in range(0, i):
        for k in range(0, j):
            for m in range(0, k):

                if i * i + j * j + k * k + m * m == n:  # 判断i,j,k,m乘以本身之和等于输入的数字
                    print('%ld*%ld+%ld*%ld+%ld*%ld+%ld*%ld=%ld' % (i, i, j, j, k, k, m, m, n))  # 是，则输出结果
                    i += 1  # 改变i的值
                    j += 1  # 改变j的值
                    k += 1  # 改变k的值
                    m += 1  # 改变m的值
                    exit(0)
