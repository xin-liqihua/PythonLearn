# 方法定义的练习

def fact(n):
	s = 1
	for i in range(1, n + 1):
		s *= i
	return s

a = fact(10)
print(a)

# 可选参数传递
def fact1(n, m = 1):
	s = 1
	for i in range(1, n + 1):
		s *= i
	return s // m
b = fact1(10) # n = 10, m = 1
print(b)
c = fact1(10, 5) # n = 10, m = 5
print(c)
# 可变参数传递
def fact2(n, *args):
	s = 1
	for i in range(1 , n + 1):
		s *= i
	for item in args:
		s *= item
	return s
d = fact2(10) # n = 10 args = []
print(d)
e = fact2(10, 3) # n = 10 args = [3]
print(e)
f = fact2(10, 3, 5, 7) # n = 10 args = [3, 5, 7]
print(f)

########################################
# 参数传递的两种方式
########################################
# 位置传递
g = fact1(10, 5) # n = 10, m = 5
print(g)
# 名称传递
h = fact1(m = 5, n = 10)# n = 10, m = 5
print(h)


#######################################
#返回值
#可有可无 有就return  XX  没有就 return
###########################################

def fact3(n, m):
	s = 1
	for i in range(1, n + 1):
		s *= i
	return s // m, n, m
i,j,k = fact3(10, 5) # i = 725760, j = 10, k = 5
print(i,j,k) 

############################################
#变量  
#局部变量 和 全局变量
############################################

l = 10
m = 100
def fact4(l):
	m = 1
	for i in range(1, l + 1):
		m *= i
	return m
print(fact4(l), m) # fact4(l) = 3628800, m = 100

def fact5(l):
	global m
	for i in range(1, l + 1):
		m *= i
	return m
print(fact5(l), m) # fact4(l) = 3628800, m = 3628800

n = ["A", "B"]
def fact6(a):
	n.append(a)
	return
fact6("C")
print(n) # ['A', 'B', 'C']

o = ["A", "B"]
def fact7(a):
	o = []
	o.append(a)
	return
fact7("C")
print(o)  #['A', 'B']


#######################################
#lambda匿名函数
########################################
p = lambda x, y : x + y
print(p(1, 10)) # 11
q = lambda : "呵呵"
print(q()) # 呵呵