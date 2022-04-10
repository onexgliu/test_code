"""
功能;递推法求数列
参数：n表示查看输出数列长度n表示查看输出数列长度
"""
def fib(n):
  a, b = 0, 1#定义a,b,并赋值0、1
  for i in range(n):#遍历数列
    a, b = b, a + b#递推求数列值，这种这种赋值，先计算等值 右边 那么属 b=1 a+b=1，再赋值给a和b，那么 a=1, b=1
  return a   #返回结果

n=int(input("请输入要查看的数列长度:"))    #用户输入查看数列长度
for i in range(0,n): #遍历
  print(fib(i), end=' ')#输出数列值
