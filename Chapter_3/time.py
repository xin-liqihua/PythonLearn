import time
scale = 10
print("-------执行开始------------")
for i in range(scale + 1):
    star = time.perf_counter()
    a = '*' * i
    b = '.' * (scale - i)
    c = ( i / scale) * 100
    time.sleep(1)
    end = time.perf_counter()
    print("{:^3.0f}%[{}->{}]   {:.5f}s".format(c,a,b,end-star))
        
    
print("--------执行结束-------------")
