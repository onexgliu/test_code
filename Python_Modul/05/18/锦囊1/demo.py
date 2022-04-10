import random  # 导入随机数模块

state = random.getstate()  # 获取当前生成器内部状态的对象
print(state)  # 打印第一次获取的生成器内容状态
random.seed()  # 系统时间作为种子，初始化生成器
random.setstate(state)  # 恢复生成器的内部状态，此处不恢复new_state将生成新的对象
new_state = random.getstate()  # 获取新生成器内部状态的对象
print(new_state)  # 打印新生成器内部状态的对象
