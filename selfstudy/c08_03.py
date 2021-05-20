a=input("입력문자열 : ")
print("출력문자열 : ",end="")

if a.startswith(" ")==True:
    print("[", end='')
print(a, end="")
if a.endswith(" ")==True:
    print("]")
    
