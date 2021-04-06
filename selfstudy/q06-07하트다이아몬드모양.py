

for i in range(0,9):
    if i<5:
    
        for k in range (0, 4-i):
            print('  ' , end='')
            k += 1
        for k in range(0,i*2+1):
            print('\u2665', end='')
            k += 1
    else :
        for k in range(0, i-4):
            print('  ', end='')
            k += 1
        for k in range(0,(9-i)*2-1):
            print('\u2665',end='')
            k += 1
    print()
    i += 1
