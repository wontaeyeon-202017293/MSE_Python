def my_print (a, b):  
    print("왼쪽:", a)      #처음에 숫자 100을 쓰더라도 직접 a 변수에 200을 바인딩해줬으므로 왼쪽: 200이 출력된다.
    print("오른쪽:", b)     #b 변수에 100을 바인딩해줬으므로 오른쪽: 100이 출력된다.

my_print(b=100, a=200)    #이것은 수업시간에 함수와 관련된 심화내용에서 배운 내용이다. a,b를 직접 바인딩하는 방법이다.