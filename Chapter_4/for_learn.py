# for .. in .. 

# 计数循环
for i in range(5):
	print(i,end=",")
	#输出结果0,1,2,3,4,
print("\n")

for i in range(1, 6, 2):
	print(i,end=",")
	#输出结果 1,3,5，
print("\n")


#列表循环
for item in [123, "Py", "aaaa", 456]:
	print(item,end=",")
	#输出结果123,Py,aaaa,456,
print("\n")

# 文件遍历
'''
for line in fi :
	<语句块>

-fi是一个文件标识符，遍历其每一行，产生循环
'''



# 保留了 break  continue 作用于java中的一样

for c in "PYTHON":
	if c=='T':
		continue
	print(c,end="")
	#输出 PYHON
print("\n")


for c in "PYTHON":
	if c=='T':
		break
	print(c,end="")
	#输出 PY
print("\n")

# 高级用法 else 用于循环没有break时调用
for c in "PYTHON":
	if c=='T':
		continue
	print(c,end="")
else:
	print("正常退出")
	#输出 PYHON正常退出

for c in "PYTHON":
	if c=='T':
		break
	print(c,end="")
else:
	print("正常退出")
	#输出 PY
print("\n")