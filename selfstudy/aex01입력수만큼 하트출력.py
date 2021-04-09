
numStr = input("각줄의 하트모양 갯수를 입력하세요 : ")

i=0
while True:
    hertNum=int(numStr[i])##첫번째 숫자를 hertNum에 넣는다.

    hertStr = ""## 합쳐서 저장되는 변수는 초기값을 설정해 주어야한다. 
    for k in range(0,hertNum):
        hertStr +="\u2665"
        k +=1

    print(hertStr)

    i +=1
    if(i>len(numStr)-1):
        break
    
