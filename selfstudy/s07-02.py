a=[]
b=[]
value =0

for i in range (0,200):
    a.append(value)
    value += 3
    

for i in range (1,201):
    b.append(a[-i]) #a리스트의 마지막수를 -1로 접근할수 있다.
        


print("b[0]: %d,  b[199]: %d " % (b[0],b[199]))
