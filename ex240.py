def 함수0(num):             #⑥이때 num은 14를 가리킨다.
    return num * 2         #⑦num * 2를 통해 28이 되고 이 값을 return시킨다.
                
def 함수1(num):             #④이때 num은 12를 가리킨다.
    return 함수0(num + 2)   #⑤함수0을 호출하는데 num + 12를 통해 num=14가 된다.
    
def 함수2(num):        
    num = num + 10        #②num=2로 바인딩되고 num + 10을 통해 num=12로 바인딩된다.
    return 함수1(num)       #③함수1을 호출한다.

c = 함수2(2)                #①함수2를 호출한다.  #⑧c에 리턴 값 28이 들어가게 된다.
print(c)                  #⑧28이 출력된다.