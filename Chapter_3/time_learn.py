import time

a=time.time()
b=time.ctime()
c = time.gmtime()
print(a,"\n",b,"\n",c,"\n")
d = time.strftime("%Y-%m-%d", c)
e = time.strptime(d, "%Y-%m-%d")
print(d,"\n",e)
