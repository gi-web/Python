a=[]
for i in range (0,4):
    a.append(0)
hap=0

for i in range (0,4):
    a[i]=int(input(str(i+1) +"번째 숫자 :"))
    
for i in range(0,4):
    hap += a[i]

print("합계 == > %d " % hap)
