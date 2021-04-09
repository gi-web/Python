import turtle

swidth, sheight =800,450

turtle.title('거북 구구단')
turtle.shape('turtle')
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)
turtle.penup()
tx, ty = -500, 250
turtle.goto(tx, ty)

for i in range(1,10):
    for k in range (2,10):
        turtle.goto(tx + 80*k, ty-40*i)
        gugu=str(k) + ' x ' + str(i) + ' = '+ str(k*i) #str()함수는 숫자를 문자로 변환
        turtle.write(gugu, font = ('Arial', 12, 'bold'))#글자형태, 크기, 진하기
