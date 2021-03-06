import numpy as np

n = np.array([0, 30, 45, 60, 90])
print('不同角度的正弦值：')
sin = np.sin(n * np.pi / 180)
print(sin)
print('计算角度的反正弦，返回值以弧度为单位：')
inv = np.arcsin(sin)
print(inv)
print('弧度转化为角度：')
print(np.degrees(inv))
