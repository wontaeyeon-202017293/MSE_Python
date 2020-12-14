#멤버함수를 이용해 sort를 하게 되면 원본 data자체가 sort되서 변하게 된다.
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

#함수(sorted)를 이용해 sort하게 되면 원본은 그대로 유지되고 다른 변수에 sort를 한 값을 바인딩해준다.
data = [2, 4, 3, 1, 5, 10, 9]
data1 = sorted(data)
print(data1)