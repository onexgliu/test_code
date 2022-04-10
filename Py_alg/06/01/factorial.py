def factorial(n):#自定义求n的阶乘函数
        if n==1:#判断n=1
                return 1#返回1结束
        else:#递归条件 即n!=1
                return n*factorial(n-1)#递归求阶乘

number = int(input("请输入一个正整数:"))#输入n的值
result = factorial(number)#调用阶乘函数
print("%d 的阶乘是 %d" %(number,result))#输出结果
