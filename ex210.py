def message1():         #message1이 A를 print하는 것을 가리킨다.
    print("A")

def message2():         #message2는 B를 print하는 것을 가리킨다.
    print("B")
                        # message3()을 해석하는 문제이다.
def message3():         # i=0일 때 message2가 호출되서 B가 출력된다.
    for i in range (3): # i=0일 때 C가 출력된다.
        message2()      # i=1일 때 message2가 호출되서 B가 출력된다.  
        print("C")      # i=1일 때 C가 출력된다.
    message1()          # i=2일 때 message2가 호출되서 B가 출력된다.
                        # i=2일 때 C가 출력되고 for문이 종료된다.   
message3()              # message1이 호출되서 A가 출력된다.
                        # ∴ B C B C B C A가 들여쓰기 형태로 순서대로 출력될 것이다.