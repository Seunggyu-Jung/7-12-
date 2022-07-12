class unit:
    def __init__(self):
        print("unit 생성자")

class flyable:
    def __init__(self) :
        print("flyable 생성자")

class flyableunit(unit,flyable):
    def __init__(self):
        super().__init__()

dropship = flyableunit()    # 다중상속일 경우, super는 다중상속 중 맨 앞의 내용만을 가져온다.