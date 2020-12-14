# 방법(1)
def print_max(a, b, c):
    if a > b and a > c:   #만약 a가 b와 c보다 크다면 a를 출력하라는 구문으로 a가 b와 c보다 크므로 가장 큰수이다.
        print(a)
    elif b > a and b > c: #if에 해당하는 부분이 참이 아니고 만약 b가 a와 c보다 크다면 b를 출력하라는 구문으로 b가 a와 c보다 크므로 가장 큰수이다.
        print(b)   
    else:                 #위의 두 구문이 모두 참이 아니라면 c를 출력하라.
        print(c)

# 방법(2)
def print_max(a, b, c):
    max_val = 0
    if a > max_val:       #만약 a가 0보다 크다면 max_val=a가 된다. 
        max_val = a
    if b > max_val:       #만약 b가 a보다 크다면 max_val=b가 된다. 크지 않다면 이 if문은 실행되지 않아 b는 max_val가 되지 않는것이다.
        max_val = b
    if c > max_val:       #만약 c가 b보다 크다면 max_val=c가 된다. 
        max_val = c
    print(max_val)
# 방법(2)에서 a=10, b=20, c=5라면 첫번째 if문으로 인해 max_val=10이 되고 2번째 if문에서 20>10이므로 실행이 되어 max_val=20이 되고 다음 if문으로 넘어간다. 3번째 if문에서 5<20이므로 if문이 실행이 되지 않아 max_val=20이 유지되고 print(max_val)를 통해 20이 출력될 것이다.


# ex) a=100, b=200, c=300
print_max(100, 200, 300)  #print_max함수를 호출하고 각 매개변수에 값을 적용했다.
