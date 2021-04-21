animal={"닭":"병아리", "개":"강아지","곰":"능소니","고등어":"고도리",
        "명태":"노가리","말":"망아지","호랑이":"개호주"}



while(True):
    wonder=input(str(list(animal.keys())) + "중 새끼이름을 알고싶은 동물은?")
    
    if wonder in animal:
        print("<%s>의 새끼는 <%s>입니다. "%(wonder, animal.get(wonder)))
    elif wonder =="끝":
        break
    else:
        print("없는 동물입니다. 동물이름을 잘 확인해 보새요")
        
