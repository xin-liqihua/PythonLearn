'''
以整数17为随机数种子，获取用户输入整数N为长度，产生3个长度为N位的密码，
密码的每位是一个数字。每个密码单独一行输出。
'''

import random

def genpwd(length):
	
    return random.randint(pow(10, length - 1), pow(10, length))

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))