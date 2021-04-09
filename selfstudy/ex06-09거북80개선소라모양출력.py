import turtle
import random

swidth, sheight, pSize = 300, 350, 3

turtle.title('거북이가 소라 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width = swidth+30, height=sheight+30)
turtle.screensize(swidth,sheight)

len = 5

for i in range (0,80):
    r=random.random();
    g=random.random();
    b=random.random();
    turtle.pencolor(r,g,b)

    turtle.forward(len)
    turtle.left(30)
    len += 1
    
    
