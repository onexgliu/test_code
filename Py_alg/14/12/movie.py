def add(a, m):
    sum = a  # 初始化求和变量
    for i in range(1, 3):
        sum += a + i * m  # 求和运算
    return sum


def mul(a, m):
    product = a  # 初始化求乘积变量
    for i in range(1, 3):
        product *= a + i * m  # 求乘积运算
    return product


def main():
    first = 0  # 初始化第一排座位数
    dif = 0  # 初始化公差
    flag = False  # 用于跳出外层循环
    for a in range(1, 36 // 3):
        m = 1
        while True:
            r = add(a, m)  # 获取求和运算结果
            if r >= 36:
                if r == 36 and mul(a, m) == 1680:
                    first = a  # 获取第一排座位数
                    dif = m  # 获取公差
                    flag = True
                break
            m += 1
        if flag:  # 如果flag为True则跳出外层循环
            break
    return first, dif


if __name__ == '__main__':
    first, dif = main()
    for i in range(10):
        print("第{}排座位数：{}".format(i + 1, first + dif * i))
