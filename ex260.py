class OMG:                  #class공간이 생기고 OMG라는 이름을 가진 변수가 바인딩한다.
    def print():            #class공간안에 print이름을 가진 함수가 생성된다. 이때 print는 어떤 함수를 바인딩한다.
        print("Oh my god")  
        
        
mystock = OMG()             #OMG()를 하면 생성자가 없기 때문에 비어있는 객체가 생성되고 이 객체는 mystock이 바인딩한다.
mystock.print()             #mystock하고 .을 찍으면 객체(mystock)가 인자로 넘어가게 된다. 즉 print(mystock)이 된다.
                            #인자가 없는 함수에 인자가 들어가기 때문에 에러가 발생하는 것이다. 따라서 def print(self)를 해줘야 에러가 발생하지 않는다.
