class stock:    #class의 이름을 stock이라고 정의함.
    def __init__(self, name, code, per, pbr, dividend):   #종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 정의했다.
        self.name = name        
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):    #self라는 객체의 종목명을 바꿀 것이다.
        self.name = name         #self의 객체 공간안에 있는 name이란 변수를 새로운 name으로 바꾼다.

    def set_code(self, code):    
        self.code = code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend 
    
 
종목 = []  # 생성한 객체를 리스트에 넣기 위해 빈 리스트를 생성한 것.

삼성전자 = stock("삼성전자", "005930", 15.79, 1.33, 2.83)    #삼성전자의 객체 생성
현대차 = stock("현대차", "005380", 8.70, 0.35, 4.27)        #현대차의 객체 생성
LG전자 = stock("LG전자", "066570", 317.34, 0.69, 1.37)    #LG전자의 객체 생성

종목.append(삼성전자)   #append멤버 함수를 통해 빈 파이썬 리스트에 삼성전자라는 변수가 가리키는 객체(stock class타입)를 대입한 것이다.
종목.append(현대차)    #append멤버 함수를 통해 빈 파이썬 리스트에 현대차라는 변수가 가리키는 객체(stock class타입)를 대입한 것이다.
종목.append(LG전자)   #append멤버 함수를 통해 빈 파이썬 리스트에 LG전자라는 변수가 가리키는 객체(stock class타입)를 대입한 것이다.

for i in 종목:       #종목이라는 리스트에는 현재 삼성전자라는 객체, 현대차라는 객체, LG전자라는 객체가 있다.
    print(i.code, i.per)  #i에 .을 찍으면 변수i에 접근할 수 있고 i는 현재 stock 클래스 타입의 객체를 바인딩하고 있다. 따라서, i에 .을 찍으면 각각의 객체의 code나 per에 접근할 수 있다. 
    