#딕셔너리의 키를 이용해 인덱싱해주면 값이 나오게 되고 이 값이 실수일 수 도 있기 때문에 float를 해준다.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price']) #최고가 - 최저가가 변동폭이기 때문에 btc안에 있는 max와 min를 float을 해준 뒤 뺀다.
시가 = float(btc['opening_price']) #btc안에 opening을 이용해 최근 24시간 내 시작 거래금액을 가져오고 float를 해준다.
최고가 = float(btc['max_price'])    #btc안에 closing을 이용해 최근 24시간 내 마지막 거래금액을 가져오고 float를 해준다.

if (시가+변동폭) > 최고가 :  #조건문: 시가+변동폭이 최고가 보다 높다면, if부분 실행 --> 상승장 도출, 시가+변동폭이 최고가 보다 낮거나 같다면, else부분 실행 --> 하락장 도출
    print("상승장")
else:
    print("하락장")
    