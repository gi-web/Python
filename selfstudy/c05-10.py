import random

a=[]
for i in range(0,10):
    a.append(random.randrange(0,10))
             
print("생성된 리스트", a)

for i in range(0,10):
    if i not in a:
        print("숫자 %d는(은) 리스터에 없네요."%i)
             
