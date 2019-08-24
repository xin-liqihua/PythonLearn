'''
获得输入的一个字符串s，以字符减号(-)分割s，将其中首尾两段用加号(+)组合后输出

etc : 输入 Alice-Bob-Charis-David-Eric-Flurry 输出 Alice+Flurry

'''
inputStr = input()
inputStr2 = inputStr.split("-")
print(inputStr2[0]+"+"+inputStr2[-1])