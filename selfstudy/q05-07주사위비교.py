import random

a = random.randrange(1,6)
print("A주사위는 %d입니다. " %a)

b = random.randrange(1,6)
print("A주사위는 %d입니다. " %b)


if a>b :
    print("%d가 이겼습니다. " %a)
elif a<b :
    print("%d가 이겼습니다. " %b)
else:
    print("비겼습니다. " )
