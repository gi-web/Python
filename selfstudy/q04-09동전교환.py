a=int(input("교환할 돈은 얼마? "))

m5man = a//50000;a=a%50000
m1man = a//10000;a=a%10000
m5chun= a//5000 ;a%=5000
m1chun = a//1000;a%=1000

m5bak = a//500  ;a%=500
m1bak = a//100  ;a%=100
m50 = a//50     ;a%=50
m10 = a//10     ;a%=10

print("50,0000원 %d장, 10,0000원 %d장,5,0000원 %d장,1,0000원 %d장"%(m5man,m1man,m5chun,m1chun))
print("500원 %d장, 100원 %d장,50원 %d장,10원 %d장"%(m5bak,m1bak,m50,m10))
print("바꾸지 못한 돈 ==> %d원" %a)
