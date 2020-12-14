result = 1               #초기값 설정, 초기값의 변수이름은 result이고 1이라는 정수가 할당되었다.   
for i in range(1, 11):   #range함수를 이용해 i가 1부터 10까지 for문이 돌도록 했다.
    result *= i          #i가 1일 때 result는 1이고 i가 2일 때 result는 2가된다. i가 3일 때 result는 6이되고 이것은 1x2x3과 같다.
print(result)            #최종적으로 i가 10일 때 result는 3,628,800이 되고 이 값은 1~10까지의 숫자들을 모두 곱한 값이다.