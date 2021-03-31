a = int(input("숫자 1:"))
b = int(input("숫자 2:"))
c = int(input("증가단위 :"))
d=0
for i in range (a, b+1 , c):
    d +=i
    
print ("%d + %d +...+%d는 %d입니다. " %(a,a+c,b,d))
