import sys

if __name__=="__main__":
    intVar = 0
    floatVar = 0.0
    blloVar=True
    strVar = ''
    listVar=[]
    tupleVar=()
    dictVar={}
    setVar = set()

    print('int형 기본 크기 -->', sys.getsizeof(intVar),'byte')
    print('float형 기본 크기 -->', sys.getsizeof(floatVar),'byte')
    print('bool형 기본 크기 -->', sys.getsizeof(blloVar),'byte')
    print('str형 기본 크기 -->', sys.getsizeof(strVar),'byte')
    print('list형 기본 크기 -->', sys.getsizeof(listVar),'byte')
    print('tuple형 기본 크기 -->', sys.getsizeof(tupleVar),'byte')
    print('dictionary형 기본 크기 -->', sys.getsizeof(dictVar),'byte')
    print('set형 기본 크기 -->', sys.getsizeof(setVar),'byte')
    
