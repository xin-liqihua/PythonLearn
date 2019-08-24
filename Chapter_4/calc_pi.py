# 计算圆周率
from random import random
from time import perf_counter

pi = 0
N = 100
for k in range(N):
	pi = pi + 1/pow(16,k)*(4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6))
print("圆周率为:{}".format(pi))


# 蒙卡特罗方法
DARTS = 1000 * 1000 #设置点数
hit = 0
start = perf_counter()
for i in range(1, DARTS + 1):
	x, y = random(), random() # 得出落点位置
	dist = pow(x**2 + y**2, 0.5) # 求出点到圆心的距离  
	if dist <= 1.0: # 判断距离是否小于半径
		hit += 1
pi2 = 4 * (hit/DARTS)
print("圆周率为:{}".format(pi2))
print("运算时间为：{:.5f}s".format(perf_counter() - start))