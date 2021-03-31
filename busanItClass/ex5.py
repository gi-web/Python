num=int(input("input number :"))
i=0
j=1
while i<num:
    j=1
    while j<=num-i:
        print("*",end='')
        j=j+1
    print()
    i=i+1
