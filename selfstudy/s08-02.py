a="<<<골<<뱅>>이>>>"
b=""

for i in range (0,len(a)):
    if a[i]!="<" and a[i]!=">":
        b += a[i]

print("a문자열:"+a)
print("b문자열:"+b)
