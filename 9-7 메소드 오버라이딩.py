class unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))


class attackunit(unit): # 상속받을 클래스에 괄호를 치고 상속받을 클래스를 작성한다.
    def __init__(self, name, hp, speed, damage):
        unit.__init__(self, name, hp, speed)   # 상속받은 클래스.__init__(self, 상속 받을 멤버변수)
        self.damage = damage
       

    def attack(self, location):
        print("{0} 유닛 : {1}방향으로 공격합니다.".format(self.name, location))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}이 파괴되었습니다.".format(self.name))

class flyable:
     def __init__(self, flying_speed):
        self.flying_speed = flying_speed

     def fly(self, name, location):
        print("{0} : {1}방향으로 날아갑니다. [속도 : {2}]".format(name, location, self.flying_speed))

class flyableattackunit(attackunit, flyable):
    def __init__(self, name, hp, damage, flying_speed):
        attackunit.__init__(self, name, hp, 0, damage)  #지상 speed = 0
        flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture = attackunit("벌처", 80, 10, 20)

battlecruiser = flyableattackunit("배틀크루저", 500, 25, 3)

vulture.move("11시")
#battlecruiser.fly(battlecruiser.name ,"9시")
battlecruiser.move("9시")  # 자식 클래스의 함수를 통해 재정의

# 메소드 오버라이딩 -> 부모클래스의 멤버 변수가 아닌 자식클래스의 멤버 변수를 사용하고 싶을때 사용하는 방법



