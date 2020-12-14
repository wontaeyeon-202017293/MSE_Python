#date를 key로 close_price를 value로 close_table이라는 딕셔너리를 만들기 위해서 먼저 변수를 설정해주고 zip이라는 함수를 통해 0번은 0번끼리 1번은 1번끼리 묶어주고 dict함수를 통해 딕셔너리로 바꿔준다.
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)