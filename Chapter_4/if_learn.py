# 计算身体质量指数BMI
height, weight = eval(input("请输入身高（米）和体重（公斤）[逗号隔开]:"))
bmi = weight / pow(height,2)
print("BMI数值为：{:.2f}".format(bmi))
res = ""
if bmi > 30 or bmi == 30:
    res = "肥胖"
elif bmi > 25:
    res = "偏胖"
elif bmi > 18.5:
    res = "正常"
else:
    res = "偏瘦"
print("国际算法中属于"+res)
res1 = ""
if bmi > 28 or bmi == 28:
    res1 = "肥胖"
elif bmi > 24:
    res1 = "偏胖"
elif bmi > 18.5:
    res1 = "正常"
else:
    res1 = "偏瘦"
print("国际算法中属于"+res1)
