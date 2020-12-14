class 부모:                #부모라는 class를 생성
  def __init__(self):    #생성자를 만든다.
    print("부모생성")

class 자식(부모):           #부모 class를 상속 받는 자식 class를 생성
  def __init__(self):
    print("자식생성")
    super().__init__()   #super()를 통해 부모 클래스에 접근하고 __init__()를 통해 부모 클래스에 있는 생성자를 호출한다. 이때 부모 클래스의 생성자의 인수는 self지만 자식클래스에 있는 self가 알아서 전달되므로 적을 필요가 없다.

나 = 자식()

#자식생성이 먼저 호출되고 super()__init__()을 통해 부모생성이 호출될 것이다.