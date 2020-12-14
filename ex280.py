#280번 만을 풀기 위해서 이보다 적은 구문만을 이용하여 해결가능하지만 나와있는 답에 대한 모든 내용을 설명하는 것이 맞다고 생각되어 최대한 다 적었습니다.

import random     #숫자를 랜덤하게 뽑기 위해 random을 import해줬다.

class Account:    #class의 이름은 Account이다.
    account_count = 0    #생성된 계좌 객체의 개수를 각각의 객체에 저장하는 것이 아닌 class에 저장하기 위해서 instance variable이 아닌 class variable를 만들었다. 초기값으로 0을 설정했다.

    def __init__(self, name, balance):
        self.deposit_count = 0      #객체가 생성되고 이를 0으로 초기화시킴. 객체가 생성된 당시에는 입금한 적이 없었기 때문이다.
        self.deposit_log = []       #self가 가리키는 공간안의 deposit_log에 접근하고 비어있는 리스트를 만든다.
        self.withdraw_log = []      #self가 가리키는 공간안의 withdraw_log에 접근하고 비어있는 리스트를 만든다.

        self.name = name            #입력받은 name을 self의 객체 공간에 저장
        self.balance = balance      #입력받은 balance를 self의 객체 공간에 저장
        self.bank = "SC은행"          #self의 객체 공간에 은행 이름을 SC은행이라고 저장한다.

        num1 = random.randint(0, 999)    # 0부터 999까지 0과 999를 포함하는 랜덤한 값을 num1이 바인딩한다.
        num2 = random.randint(0, 99)     # 0부터 99까지 0과 99를 포함하는 랜덤한 값을 num2가 바인딩한다.
        num3 = random.randint(0, 999999) # 0부터 999999까지 0과 999999를 포함하는 랜덤한 값을 num3이 바인딩한다.

        num1 = str(num1).zfill(3)        # 랜덤한 값을 바인당한 변수 num1을 문자열로 바꾸고 zfill(자릿수를 맞추기 위해 앞에 0을 대입함)을 통해 자릿수를 맞춰줬다.
        num2 = str(num2).zfill(2)  
        num3 = str(num3).zfill(6)  
        
        self.account_number = num1 + '-' + num2 + '-' + num3  # 3자리-2자리-6자리의 계좌번호가 self의 객체 공간에 account_number를 만들고 이를 바인딩한다.
        Account.account_count += 1  #Account 클래스에 .을 찍어 접근한 후 공간안에 있는 account_count란 변수에 접근하고 계좌가 개설될 때마다 1씩 증가하도록 했다.

    @classmethod
    def get_account_num(cls):       #account_count는 객체가 아닌 클래스에 저장되어 있기 때문에 self가 필요하지 않다.
        print(cls.account_count)    #일반적으로 a.get_account_num()을 하게 되면 파이썬에서 자동으로 Account.get_account_num(a)로 변경한다. 하지만 인자가 없는 함수에 인자가 들어가게 되므로 에러가 발생한다.
                                    #객체에 접근할 필요가 없는 것들(데이터가 객체가 아닌 class에 저장되어 있는 것들)을 classmethod이용하여 구문을 구성한다. cls자리에 객체가 아닌 클래스의 이름이 넘어오는 방식이다.
    def deposit(self, amount):      #잔고는 객체에 저장되기 때문에 객체에 접근하기 위해 self를 이용했다. 입금액을 account로 바인딩했다.
        if amount >= 1:             #입금은 1원 이상부터 가능!!
            self.deposit_log.append(amount)  #self가 가리키는 공간에 있는 deposit_log에 접근하고 비어 있는 리스트에 amount를 append한다. 입금 내역을 저장하는 것이다!!
            self.balance += amount  #self가 가리키는 공간에 있는 balance에 amount를 추가하면 된다.

            self.deposit_count += 1 #입금이 되면 deposit_count를 1증가시킨다.
            if self.deposit_count % 5 == 0:   #deposit_count가 5의 배수가 되면 이자 1%가 지급되어야 한다.
                self.balance = (self.balance * 1.01) #deposit_count가 5의 배수가 되어서 실행되는 문장으로 balance변수가 가리키는 값에 1.01을 곱해 이자를 주고 이 값을 다시 balance가 바인딩 한다.


    def withdraw(self, amount):     #객체 공간에 접근하기 위해 self를 적고 얼마를 출금할 건지에 대한 amount를 적었다. 
        if self.balance > amount:   #마이너스 통장에서는 이와 같은 구문이 필요 없지만, 일반적인 통장에서는 잔고에 출금하는 금액 이상이여야 출금이 가능하다.
            self.withdraw_log.append(amount) #self가 가리키는 공간에 있는 withdraw_log에 접근하고 비어 있는 리스트에 amount를 append한다. 출금 내역을 저장하는 것이다!!
            self.balance -= amount  #입금과 달리 잔고에서 금액을 빼면 된다.

    def display_info(self):                   
        print("은행이름: ", self.bank)           #self가 가리키는 객체인 bank에 저장되어 있는 은행이름이라는 변수에 접근하고 그 값을 출력한다.
        print("예금주: ", self.name)            #self가 가리키는 객체인 name에 저장되어 있는 예금주라는 변수에 접근하고 그 값을 출력한다.
        print("계좌번호: ", self.account_number) #self가 가리키는 객체인 account_number에 저장되어 있는 계좌번호라는 변수에 접근하고 그 값을 출력한다.
        print("잔고: ", self.balance)           #self가 가리키는 객체인 balance에 저장되어 있는 잔고라는 변수에 접근하고 그 값을 출력한다.

    def withdraw_history(self):
        for amount in self.withdraw_log:    #self가 가리키는 객체 공간안에 있는 withdraw_log에 접근하여 출금 내역을 출력한다.
            print(amount)

    def deposit_history(self):
        for amount in self.deposit_log:     #self가 가리키는 객체 공간안에 있는 deposit_log에 접근하여 입금 내역을 출력한다.
            print(amount)
            
# deposit_history와 withdraw_history를 호출해 지금까지의 입금 내역과 출금 내역을 출력하기 위한 코드를 작성하는 것이 280번의 목적이다.
k = Account("Kim", 1000)
k.deposit(100)    #k에 100원 입금
k.deposit(200)    #k에 200원 입금
k.deposit(300)    #k에 300원 입금
k.deposit_history()  #함수를 실행해서 입금 내역을 본다.

k.withdraw(100)   #k에서 100원 출금
k.withdraw(200)   #k에서 200원 출금
k.withdraw_history()  #함수를 실행해서 출금 내역을 본다.