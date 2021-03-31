import turtle

swidth, sheight = 500,500

turtle.title("무지개")
turtle.shape('turtle')
turtle.setup(width = swidth+50, height = sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.goto(0,-sheight/2)
turtle.pendown()
turtle.speed(15)

for i in range(1, 250):##i는 원의 반지름크기 249까지 증가
    if i % 6 == 0:
        turtle.pencolor('red')
    elif i%5 == 0:
        turtle.pencolor('orange')
    elif i%4 == 0:
        turtle.pencolor('yellow')
    elif i%3 == 0:
        turtle.pencolor('green')
    elif i%2 == 0:
        turtle.pencolor('blue')
    elif i%1 == 0:
        turtle.pencolor('navyblue')
    else :
        turtle.pencolor('purple')

    turtle.circle(i)

