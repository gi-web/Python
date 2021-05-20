a = "  즐 겁 고 건 강 하게 "
b=""

for i in range(0,len(a)):
    if a[i] !=" ":
        b += a[i]

print("처음문자열 : "+a)
print("공백삭제후 문자열 ; "+b)
