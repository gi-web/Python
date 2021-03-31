import turtle
import math
import random

swidth, sheight = 300,300

turtle.title('거북이 만나기')
turtle.setup(width=swidth + 50, height=sheight+50)
turtle.screensize(swidth,sheight)

t1 = turtle.Turtle('turtle')##거북이 생성
t1.color('red');t1.penup()
t2=turtle.Turtle('turtle');t2.color('green');t2.penup()
t3=turtle.Turtle('turtle');t3.color('blue');t3.penup()

t1.goto(-100,-100); t2.goto(0,0);t3.goto(100,100)
while True:
    angle = random.randrange(0, 360)
    dist = random.randrange(1, 50)
    t1.left(angle); t1.forward(dist)
    angle=random.randrange(0,360)
    dist=random.randrange(1,50)
    t2.left(angle);t2.forward(dist)
    angle=random.randrange(0,360)
    dist=random.randrange(1,50)
    t3.left(angle);t3.forward(dist)

    t1x=t1.xcor(); t1y=t1.ycor() ##x, y 좌표를 변수에 넣어 준다.
    t2x=t2.xcor(); t2y=t2.ycor()
    t3x=t3.xcor(); t3y=t3.ycor()

    if math.sqrt(((t1x-t2x)*(t1x-t2x))+((t1y-t2y)*(t1y-t2y)))<=20 or\
       math.sqrt(((t1x-t3x)*(t1x-t3x))+((t1y-t3y)*(t1y-t3y)))<=20 or\
       math.sqrt(((t2x-t3x)*(t2x-t3x))+((t2y-t3y)*(t2y-t3y)))<=20 :
        t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3)
        break
    if  (-swidth/2 > t1x or t1x > swidth/2) or (-sheight/2 > t1y or t1y > sheight/2):
        t1.goto(-100,-100)
    if  (-swidth/2 > t2x or t2x > swidth/2) or (-sheight/2 > t2y or t2y > sheight/2):
        t2.goto(0,0)
    if  (-swidth/2 > t3x or t3x > swidth/2) or (-sheight/2 > t3y or t3y > sheight/2):
        t3.goto(100,100)
        

    