import random

data =[]
i,k=0,0

if __name__=="__main__":
    for i in range(0,10):
        tmp = hex(random.randrange(0,100000))
        data.append(tmp)

    print('전렬 전 데이터:',end='')#줄바꿈 하지않음
    [print(num+',',end='') for num in data]#리스트 컴프리헨션 문장

    for i in range(0,len(data) -1):
        for k in range(i+1, len(data)):
            if int(data[i],16) > int(data[k],16): # 16진수인 data를 10진수로 변경,오름차순으로 정렬
               #temp=data[i]
               #data[i]=data[k]
               #data[k]=temp
               data[i],data[k]=data[k],data[i]
    print('\n정렬후 데이터 :',end='')
    [print(num+',', end='') for num in data]#data안에 데이터를 num에 데이터가 없을때까지 반복해서 넣어서 출력해주는것 같음
    
    
                       
    
                   
