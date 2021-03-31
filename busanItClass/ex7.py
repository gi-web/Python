import random

arr=set()
while len(arr)<7:
    arr.add(random.randint(1,50))
print("생성된 집합 :",arr)    
print("집합에서 가장 큰 수 :",max(arr))
print("집합에서 가장 작은 수 :",min(arr))
