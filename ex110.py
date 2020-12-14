# 첫번째 if문의 조건이 True이므로 print("4")부분, 즉 첫번째 else부분을 실행되지 않고 두번째 if문이 시작된다. 
# 두번째 조건문은 False이므로 else부분이 실행되어 3이 출력될 것이다.
# 또한 if-else문이 끝난 뒤 공통부분인 print("5")가 실행되어 결과값으로 3과 5가 출력될 것이다.
if True:           #조건문이 True이므로 if부분 실행
    if False:      #조건문이 False이므로 else부분 실행
        print("1")
        print("2")
    else:          #else부분이 실행되어 3이 출력된다.
        print("3")
else:
    print("4")
print("5")         #공통부분으로 5가 출력된다.
        