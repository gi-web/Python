a=[]
for i in range (0,10):
    a.append(0)
hap=0

for i in range (0,10):
    a[i]=int(input(str(i+1) +"번째 숫자 :"))

    
i=0
while i<10 :
    hap += a[i]
    i+=1

print("합계 == > %d " % hap)
