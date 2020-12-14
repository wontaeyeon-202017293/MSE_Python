#try:
#    실행 코드
#except:
#    예외가 발생했을 때 수행할 코드
#else:
#    예외가 발생하지 않았을 때 수행할 코드
#finally:
#    예외 발생 여부와 상관없이 항상 수행할 코드


per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))  
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")

#①첫번째로 10.31이라는 문자열을 try해 10.31이 출력될 것이고, 10.31은 실수이므로 예외가 발생하지 않았으므로 else가 수행되어 clean data가 출력될 것이고, 예외 발생 여부에 상관없이 finally가 수행되어 변환 완료가 출력될 것이다.
#②공백 문자열이므로 try를 하면 예외가 발생하게 된다. 따라서 except가 수행되어 0이 출력되고 finally를 통해 변환 완료가 출력될 것이다.
#③8.00은 10.31과 같은 방식으로 순서대로 들여쓰기 형식으로 8.0, clean data, 변환 완료가 출력될 것이다.
