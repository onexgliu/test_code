for a in range(0, 1001):  # 遍历a
    for b in range(0, 1001):  # 遍历b
        for c in range(0, 1001):  # 遍历c
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:  # 条件
                print("a, b, c:", a, b, c)  # 输出结果
