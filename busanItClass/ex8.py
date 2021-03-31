import find

a=int(input("첫 번째 숫자 :"))
b=int(input("두 번째 숫자 :"))
c=int(input("세 번째 숫자 :"))

print("가장 큰 수 :",find.findMax(a,b,c))
print("가장 작은 수 : ",find.findMin(a,b,c))
print("숫자의 합: ",find.findSum(a,b,c))

