# if-else문과 values멤버함수를 이용해 코딩한다.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")
if user in fruit.values():   #딕셔너리 값을 이용하므로 values를 이용!
    print("정답입니다.")
else:
    print("오답입니다.")