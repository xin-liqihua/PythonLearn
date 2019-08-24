# 画一条蛇
import turtle
turtle.setup(650,350,200, 200) # 设置窗口
turtle.penup() # 抬起画笔  画笔移动不留下痕迹
turtle.fd(-250)
turtle.pendown()# 画笔放下  
turtle.pensize(10)
turtle.pencolor("blue")
turtle.seth(-40)
for i in range(4):
	#turtle.circle(r，L) 画一个圆心在画笔当前位置的正左上方(r为负值时为右下方),半径为r 弧度为L的圆(L=180即画一个半圆, 起点为当前位置) 
    turtle.circle(40,80) 
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40* 2/3)
turtle.done()
