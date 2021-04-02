while True:
    a = int(input("계산할 첫 번째 수: "))
    b = int(input("계산할 두 번째 수: "))
    c = input("계산할 연산자를 입력하세요 :")

    if (c=="+"):
        print("%d + %d = %d" %(a,b,a+b))
    elif (c=="-"):
        print("%d - %d = %d" %(a,b,a-b))
    elif (c=="*"):
        print("%d * %d = %d" %(a,b,a*b))
    elif (c=="/"):
        print("%d / %d = %d" %(a,b,a/b))
    else :
        print("연산자를 잘못 입력했습니다.")
        
        
