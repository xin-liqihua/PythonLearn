# 一到五进步 星期6 7 退步 
# 计算星期一到五每天进步多少  才能和 每天进步0.01相同 
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("{:.3f}".format(dayfactor))

