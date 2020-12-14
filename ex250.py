import numpy                      #일반적인 for i in range는 정수단위로만 증가가 가능하기 때문에 numpy를 import하여 0.1과 같은 실수 단위로 증가시킨다.
for i in numpy.arange(0, 5, 0.1): #numpy라는 모듈의 arange를 사용하여 실수단위로 증가시킨다. (0, 5, 0.1)은 0부터 5까지 0.1의 단위로 증가하는 것이다.
    print(i) 