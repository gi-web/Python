import operator  ##정렬기능을 사용하기 위해 import

a='''계절이 지나가는 하늘에는 가을로 가득차 있습니다.
나는 아무 걱정도 없이 가을속의 별들을 다 헤일듯 합니다.
가슴속에 하나 둘 새겨지는 별을 이제 다 못헤는 것은
쉬이 아침이 오는 까닭이요.
내일 밤이 남은 까닭이요.
아직 나의 청춘이 다하지 않은 까닭입니다.

별하나에 추억과
별하나에 사랑과
별하나에 쓸쓸함과
별하나에 동경과
별하나에 시와
별하나에 어머니, 어머니'''

cDic={}
cList=[]

for ch in a:
    if "가" <= ch and ch <= "힣": ## 문자가 한글 범위에 있는지
        if ch in cDic:
            cDic[ch] += 1
        else:
            cDic[ch] =1

cList=sorted(cDic.items(), key=operator.itemgetter(1),##딕셔너리의 값을 기준으로 정렬##
             reverse=True )##내림차순##

print("원문\n",a)
print("--------------------")
print("문자\t 빈도수")
print("----------------------")
for i in range(0,len(cList)):
    print(cList[i][0],"\t",cList[i][1])
    
