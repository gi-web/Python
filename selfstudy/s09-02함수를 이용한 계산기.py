##함수활용 계산기 구현##

##함수 선언##
def clock(num1,num2,op):
    result=0
    if op=="+":
        result=num1+num2
    elif op=="-":
        result=num1-num2
    elif op=="*":
        result=num1*num2
    elif op=="/":
        result=num1/num2
    elif op=="**":
        result=num1**num2
    return result

##함수 사용##
num1=int(input("첫 번째 수를 입력하세요:"))
op=input("계산을 입력하세요(+,-,*,/,**)")
num2=int(input("두 번째 수를 입력하세요:"))
if op=="/" and num2==0:
    print("0으로 나나누면 안됍니다.ㅠㅠ")
else:
    result=clock(num1,num2, op)
    print("##계산기##")
    print("%d %s %d = %d"%(num1,op,num2,result))
        
