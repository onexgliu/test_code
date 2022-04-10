for step in range(1,1000):
    #判断阶梯条件
    if (step % 2 == 1) and (step % 3 == 2) and (step % 5 == 4) and (step % 6 == 5) and (step % 7 == 0):
        print('可能有', step, '层台阶')#输出满足阶梯条件的数
        step += 1#阶梯数加1再进入循环
    else:#不满足阶梯条件
      step += 1#也要将阶梯数加1再进入循环

