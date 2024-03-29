#获得用户输入数字N，计算并输出从N开始的5个质数，单行输出，质数间用逗号,分割。

def prime(m):
    end = int(pow(m, 0.5) + 1)
    for i in range(2, end):
        if m%i == 0:
            return False
    else:
        return True

n = eval(input())
if n != int(n):  # 因为可能输入有浮点数
    n = int(n) + 1
else:  # 保证输入5.0时，输出为整数5。这里只根据题目中只输入正浮点或者正整数时做的处理
    n = int(n)  
count = 5
while count > 0:
    if prime(n):
        if count > 1:
            print(n, end=',')
        else:
            print(n)
        count -= 1
    n += 1

