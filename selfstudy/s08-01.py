string='파이썬은완전재미있어요'

for i in range(0,len(string)):
    if i%2 == 0:
        print(string[i],end='')
    else:
        print("#",end='')
