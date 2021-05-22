##지역변수, 전역변수,global예약어##
def func4():
     print("func4에서 a값:%d"%a)
def func1():
    global a#a를 전역변수로 지정해 지역변수 a는 존재하지 않는다.
    a=10 #지역변수
    print("func1에서 a값:%d"%a)
def func2():
    a=10 #지역변수
    print("func2에서 a값:%d"%a)
def func3():
    print("func3에서 a값:%d"%a)

a=20 #전역변수

##함수사용##
func4()
func1()
func2()
func3()



    
