a=[]
b=[]
value=1
for i in range(0,3):
    for k in range(0,4):
        a.append(value)
        value +=1
    b.append(a)
    a=[]

for i in range(0,3):
    for k in range(0,4):
        print("%3d"%b[i][k],end="")#행을 넘기지 않고 출력
    print("")#행변경
