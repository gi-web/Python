c=""

a=input("문자열 입력-->")
count=len(a)

for ch in a:
    if (ord(ch)>=ord("A") and ord(ch)<=ord("Z")):  #ord(문자):문자를 숫자로변환 
        b=ch.lower()
    elif (ord(ch)>=ord("a") and ord(ch)<=ord("z")):
        b=ch.upper()
    else:
        b=ch

    c += b
print("대소문자 변환 결화 --> %s" %c)
        
