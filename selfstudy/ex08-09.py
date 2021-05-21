
import turtle
import random
from tkinter.simpledialog import *
import math

sw=400
sh=400


turtle.title("거북 원 모양의 글자 쓰기")
turtle.shape("turtle")
turtle.setup(width=sw+50, height=sh+50)
turtle.penup()



a=askstring("문자입력","원모양으로 출력할 문자열 입력")

dis=100 ##원의 반지름은 100으로 한다
ang=0
gapAng=360/len(a)#360에서 문자열 갯수만큼 나누어 하나씩 출력


for ch in a:
    rad=3.14*ang/180  #cos()및sin()함수의 각도은 라디안 값으로 처리 공식 문제에서 알려줌
    sx=dis*math.cos(rad) #x좌표 구하는 공식
    sy=dis*math.sin(rad) #y좌표 구하는 공식
    ang += gapAng
    r=random.random();g=random.random();b=random.random()
    tSize = 20  ##글자크기는 20으로 한다.

    turtle.goto(sx,sy)
    turtle.pencolor(r,g,b)
    turtle.write(ch, font=("둥글레",tSize,'bold'))

turtle.done
    
