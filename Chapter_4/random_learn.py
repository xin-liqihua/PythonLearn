import random
random.seed(10)
print(random.random())
random.seed(10)
print(random.random())
'''
输出结果
0.5714025946899135
0.5714025946899135
设置随机种子  可以再现随机结果
不设置  默认使用random.random()时系统的时间为随机种子 即很难再现随机结果
'''

print(random.randint(1,10)) #生成一个【1,10】之间的随机整数
print(random.randrange(1,10,2)) # 生成一个【1,10】之间以2为步长的随机整数
print(random.getrandbits(16)) #生成一个16比特从的随机整数
print(random.uniform(1,10)) #生成[1,10]之间的随机小数
print(random.choice([1,2,3,4,5,6,7,8])) #在 [1,2,3,4,5,6,7,8] 随机一个
# 打乱[1,2,3,4,5,6,7,8] 的排列顺序
s=[1,2,3,4,5,6,7,8]
random.shuffle(s)
print(s)