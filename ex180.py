low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

#방법1
volatility = []   #빈 리스트 생성
for i in range(len(high_prices)):  #len함수를 이용한다 --> high_prices 리스트안의 원소의 개수가 5개이므로 len(high_prices)=5이다.
    volatility.append(high_prices[i] - low_prices[i])  #i는 0~4까지 변하므로 0~4번째 high_prices의 원소의 값 - 0~4번째 low_prices의 원소의 값을 하여 volatility의 빈 리스트안에 append 멤버함수를 통해 추가한다.
print(volatility)                  

#방법2
volatility = []
for i in range(5):   #자체적으로 5개임을 파악한 후 5를 적었다. 이것은 처음 주어진 리스트안의 원소의 개수를 셀 수 있을 때 유용하다.
    diff = high_prices[i] - low_prices[i]   #방법1과 똑같은 방식으로 diff라는 이름을 가진 변수에 high_prices와 low_prices의 차를 집어 넣는다.
    volatility.append(diff)     #volatility의 빈 리스트안에 append 멤버함수를 이용하여 추가하는데 여기서는 직접 차를 적지 않고 diff라는 변수를 생성한 후 변수를 괄호안에 넣는 방법을 택했다.  
print(volatility)  