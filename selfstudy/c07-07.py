import turtle
import random

myTurtle, tx, ty,tcolor, tsize,tshape=[None]*6
shapeList=[]
playerTurtles=[]
swidth, sheight = 500,500

if __name__ == "__main__":
    turtle.title("거북리스트 활용")
    turtle.setup(width=swidth+50, height=sheight+50)
    turtle.screensize(swidth,sheight)

    shapeList=turtle.getshapes()#allow,blank, circle,classic,square,trangle,turtle등 7개 종류 추출
    for i in range(0,100) :
        random.shuffle(shapeList)#shapeList를 섞어준다=tmShape=random.choice(shapeList)
        myTurtle=turtle.Turtle(shapeList[0])#첫번째모양으로 사용한다.=myTurtle=turtle.Turtle(tmShape)
        tx = random.randrange(-swidth/2, swidth/2)
        ty = random.randrange(-sheight/2, sheight/2)
        r = random.random(); g=random.random();b=random.random()
        tSize=random.randrange(1,3)
        playerTurtles.append([myTurtle, tx, ty, tSize,r,g,b])

    for tList in playerTurtles:#playerTurtles에있는것을 하나씩 tList에 넣어준다
        myTurtle=tList[0]
        myTurtle.color(tList[4],tList[5],tList[6])
        myTurtle.pencolor(tList[4],tList[5],tList[6])
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1],tList[2])
    turtle.done()
                             
        
        
    
    
