a=input("문자 와 숫자입력:")
b=""


for i in range(0,len(a)):
    if a[i].isalpha():
        b += a[i]

print("숫자 제거 문장: " + b)
