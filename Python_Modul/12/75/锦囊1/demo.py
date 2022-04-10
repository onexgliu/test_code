import sys

print('默认：', sys.get_coroutine_origin_tracking_depth())
sys.set_coroutine_origin_tracking_depth(10)
print('设置后：', sys.get_coroutine_origin_tracking_depth())
