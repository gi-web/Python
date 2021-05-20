import turtle
import random
from tkinter.simpledialog import * ##askstring()함수사용가능하게 해준다##

a=""
sw, sh = 300, 300
sx,sy,tSize=[0]*3

turtle.title("거북이 입력받은 글자 랜덤하게 크기,위치,색상 출력")
turtle.shape("turtle")
turtle.setup(width=sw +50, height=sh+50)
turtle.screensize(sw,sh)
turtle.penup()

a=askstring("문자열입력", "거북이 쓸 문자열을 입력") ##turtle그래픽에서 문자열을 입력받는다

for ch in a : #a에서 한글자씩꺼내 ch에 넣는다
    sx=random.randrange(-sw/2,sw/2)
    sy=random.randrange(-sh/2,sh/2)
    r=random.random();g=random.random();b=random.random()
    tSize=random.randrange(10,50)

    turtle.goto(sx,sy)

    turtle.pencolor(r,g,b)
    turtle.write(ch,font=("둥글레",tSize,"bold"))

turtle.done()

    

