import turtle
import random

swidth, sheight, pSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY=[0]*7

turtle.title('거북 맘대로 다니기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width = swidth + 30, height = sheight + 30)##윈도우창 폭과 높이
turtle.screensize(swidth, sheight)##안쪽화면 크기

while True:
    r=random.random()
    g=random.random()
    b=random.random()
    turtle.pencolor(r,g,b)

    angle=random.randrange(0,360)## 각도
    dist=random.randrange(1,100)##거리
    turtle.left(angle)
    turtle.forward(dist)
    curX=turtle.xcor()##현재위치
    curY=turtle.ycor()

    if (-swidth/2 <= curX and curX <= swidth/2) and (-sheight/2 <= curY and curY <= sheight/2):
        pass ##if문 종료하고 다시  while문 수행
    else:
        turtle.penup()##펜을 들었기 때문에 그리기가 안되고 이동
        turtle.goto(0,0)
        turtle.pendown()##다시 이동 하면 그려 진다.

        exitCount +=1
        if exitCount >= 5 :
            break ##while문을 빠져 나간다.
turtle.done() ##프로그램 종료
        
        
    

             
            
