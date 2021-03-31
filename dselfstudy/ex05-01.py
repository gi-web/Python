import random
allCount = 0
throwCount = 0

while True:
    allCount += 1

    a = random.randrange(1,7)
    b = random.randrange(1,7)
    c = random.randrange(1,7)
    d = random.randrange(1,7)
    e = random.randrange(1,7)
    f = random.randrange(1,7)

    if a==b==c==d==e==f:
        print("6개의 주사위가 모두 동일한 숫자가 나옴-->",a,b,c,d,e,f)
        break
    elif (1==a or 1==b or 1==c or 1==d or 1==e or 1==f) and\
         (2==a or 2==b or 2==c or 2==d or 2==e or 2==f) and\
         (3==a or 3==b or 3==c or 3==d or 3==e or 3==f) and\
         (4==a or 4==b or 4==c or 4==d or 4==e or 4==f) and\
         (5==a or 5==b or 5==c or 5==d or 5==e or 5==f) and\
         (6==a or 6==b or 6==c or 6==d or 6==e or 6==f) :
        throwCount +=1
print("6개의 동일한 숫자가 나올때까지 던지 횟수-->",  allCount)
print("6개의 동일한 숫자가 나올때까지 1~6의 연속번호가 나온 횟수-->",throwCount)
        
    
    
