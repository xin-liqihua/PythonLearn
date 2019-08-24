# 汉诺塔
# 递归函数学习

count = 0
def hanoi(n, src, dst, mid):
	global count
	if n == 1:
		print("{}:{}->{}".format(src, 1, dst))
		count += 1
	else:
		hanoi(n-1, src, mid, dst)
		print("{}:{}->{}".format(src,n,dst))
		count += 1
		hanoi(n-1, mid, dst, src)
hanoi(5, "A", "B", "C")
print(count)