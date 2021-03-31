import turtle

turtle.title('거북이로 2진수 표현하기')
turtle.shape('turtle')
swidth = 1000
sheight = 300
turtle.setup(width=swidth+50, height=sheight + 50)##윈도우 화면크기
turtle.screensize(swidth,sheight)##스크린 화면 크기
turtle.penup()
turtle.left(90)##거북이 왼쪽으로 90도 회전

a=int(input(" 숫자를 입력하세요"))
b=bin(a) ##입력된 숫자를 2진수 문자열로 변환
print(b)
x=swidth/2 ##x좌표는 화면 제일 끝
y=0
for i in range(len(b)-2): ##이진수로 변환되면 ob숫자 로 표현됨으로 ob길이만큼 뺀다.
    turtle.goto(x,y)
    if a&1:
        turtle.color('red')
        turtle.turtlesize(2)
    else :
        turtle.color('blue')
        turtle.turtlesize(1)
    turtle.stamp()
    x -=50
    a >>=1

        



