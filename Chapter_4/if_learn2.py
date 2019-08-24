# 计算BMI值2
height,weight = eval(input("请输入身高（米）和体重（公斤）[逗号隔开]:"))
bmi = weight / pow(height,2)
print("BMI数值为：{:.2f}".format(bmi))
world, china = "", ""
if bmi < 18.5:
    world, china = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    world,china = "正常", "正常"
elif 24 <= bmi < 25:
    world, china = "正常", "偏胖"
elif 25 <= bmi < 28:
    world, china = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    world, china = "偏胖", "肥胖"
else:
    world, china = "肥胖", "肥胖"
print("世界标准{},国内标准{}".format(world, china))
