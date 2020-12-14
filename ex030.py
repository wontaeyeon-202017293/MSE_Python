#replace 멤버 함수를 사용하면 원본인 abcd가 바뀌는 게 아니라 새롭게 aBcd가 생긴다. 따라서 string은 여전히 abcd를 가리키기 때문에 화면에는 abcd가 출력될 것이다.
string = 'abcd'
string.replace('b', 'B')
print(string) #abcd가 출력될 것으로 예상된다.