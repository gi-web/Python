a = input("문자열을 입력하세요:")
if a.isalpha() :
    print("글자입니다")
elif a.isdigit():
    print("숫자입니다")
elif a.isalnum():
    print("글자+숫자입니다")
else :
    print("모르겠습니다.")
                
