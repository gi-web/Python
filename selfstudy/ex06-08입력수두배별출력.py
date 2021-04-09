
a=input("별오양갯수 나누기 2한 숫자를 입력: ")

i = 0

while True:

    starNum=int(a[i])
    starStr=""
    
    for k in range(0, starNum*2):
        starStr += "\u2605"

    print(starStr)

    i += 1
    if( i > len(a)-1):
        break
        

        
