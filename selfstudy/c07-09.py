import operator

dic, dicList={},[]
dic = {'apple':'사과', 'banana':'바나나', 'strawbary':'딸기'}
dicList=sorted(dic.items(),key=operator.itemgetter(0))#키를 기준으로 dic를 정렬한다.
print(dicList)

dicList=sorted(dic.items(),key=operator.itemgetter(1))#값을 기준으로 dic를 절렬한다.
print(dicList)
