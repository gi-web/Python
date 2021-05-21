a=input("문자열을 입력:")
b,c,d,e,f=0,0,0,0,0

for i in range(0, len(a)):
    if a[i].isdigit():
        b += 1
    elif (ord(a[i]) >= ord("A") and ord(a[i]) <= ord("Z")):
        c += 1
    elif (ord(a[i]) >= ord("a") and ord(a[i]) <= ord("z")):
        d += 1
    
    elif a[i] >= "가" and a[i]<="힣":
        e += 1
    else:
        f += 1

print("숫자:%d  대문자:%d  소문자:%d   한글:%d  기타문자:%d "%( b,c,d,e,f))
        
    
        
