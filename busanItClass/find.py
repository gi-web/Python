#find.py모듈 이용
def findMax(a,b,c):
    if a>b:
        big=a
    else:
        big=b
    if big<c:
        big=c
    return big

def findMin(a,b,c):
    if a<b:
        sam=a
    else:
        sam=b
    if sam>c:
        sam=c
    return sam

def findSum(a,b,c):
    return a+b+c
    
        