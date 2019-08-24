'''
四位玫瑰数是4位数的自幂数。自幂数是指一个 n 位数，它的每个位上的数字的 n 次幂之和等于它本身。
请输出所有4位数的四位玫瑰数，按照从小到大顺序，每个数字一行。
'''

for i in range(1000,10000):
    a = i//1000
    b = (i- a * 1000)// 100
    c = (i- a * 1000 - b * 100)// 10
    d = i-a*1000-b*100-c*10
    if pow(a,4)+pow(b,4)+pow(c,4)+pow(d,4)==i:
        print(i)


s = ""
for i in range(1000, 10000):
    t = str(i)
    if pow(eval(t[0]),4) + pow(eval(t[1]),4) + pow(eval(t[2]),4) + pow(eval(t[3]),4) == i :
        print(i)