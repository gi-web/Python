#문자열 입력받아 반대로 출력

inStr,outStr="",""

inStr=input("문자열을 입력하세요: ")

for i in range(0,len(inStr)):
    print(inStr[len(inStr)-1-i],end='')
    
