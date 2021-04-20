a=[]
b=[]
value=0
for i in range(0,4):
    for k in range(0,5):
        a.append(value)
        value +=3
    b.append(a)
    a=[]

for i in range(0,3):
    for k in range(0,4):
        print("%3d"%b[i][k],end="")#행을 넘기지 않고 출력
    print("")#행변경
