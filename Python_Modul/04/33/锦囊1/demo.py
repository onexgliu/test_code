import math  # 导入数学模块

print(math.isclose(5, 6))
print(math.isclose(5, 6, rel_tol=1))
print(math.isclose(6, 6))
print(math.isclose(3.14, 3.21))
print(math.isclose(3.14, 3.21, rel_tol=0.7))
