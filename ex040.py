# strip()멤버함수를 이용하여 공백을 제거하는데, 여기서 이전 문제인 30번의 replace와 같이 원본 개체는 그대로 유지되고 strip으로 인해 공백이 사라진 문자열을 data1에 바인딩 즉 변수의 메모리에 할당해 고정시키고 이를 print하면 공백이 제거된 문자열이 나온다.
data = "   삼성전자   "
data1 = data.strip()
print(data1)