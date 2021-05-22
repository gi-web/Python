##커피자판기 사용을 함수를 이용하용하여 표현
##함수 선언##
def coffee_machine(user):
    print("*********커피주문*********")
    button=int(input(user+"씨 어떤커리를 드릴까요?(1:아메리카노, 2:카페라떼 3:카푸치노 4:에스프레소)"))
    print("#1.뜨거운물준비")
    print("#2.종이컵 준비")

    if button==1:
        print("#3.아메리카노 커피를 만든다")
    elif button==2:
        print("#3 까페라떼 커피를 만든다")
    elif button==3:
        print("#3 카푸치노 커피를 만든다")
    elif button==4:
        print("#3 에스프레소 커피를 만든다.")
    
    print("#4 물을 붓는다")
    print("#5.스푼으로 젖는다.")
    print(user+"씨~  커피 여기 있습니다.")
    print("-----------------------------")

##함수사용##

coffee_machine("로제")
coffee_machine("리사")
coffee_machine("지수")
coffee_machine("제니")


    
