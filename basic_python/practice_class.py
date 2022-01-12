from random import *


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} unit is made".format(name))

    def move(self, location):
        print("[ground unit move]")
        print("{0} : {1} way to move [speed {2}]".format(
            self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} damaged".format(self.name, damage))
        self.hp -= damage
        print("{0} : current hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : destroied".format(self.name))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} way to attack anemy. [damage {2}]".format(
            self.name, location, self.damage))


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "marine", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            print("{0} : use stimpack. (Hp 10 decrese)".format(self.name))
        else:
            print(
                "{0} : Hp is less then 10, not enough to user stimpack".format(self.name))


class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{0} : turn seize mode on". format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : turn seize mode off". format(self.name))
            self.damage /= 2
            self.seize_mode = False


class Flyable:
    def __init__(self, flying_speed):
        self. flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} way to fly. [speed {2}]".format(
            name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[air unit move]")
        self.fly(self.name, location)


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "wraith", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : turn clocking mode off".format(self.name))
            self.clocked == False
        else:
            print("{0} : turn clocking mode on".format(self.name))
            self.clocked == True


def game_start():
    print("[notice] start new game")


def game_oveer():
    print("Player : gg")
    print("[Player] is exit the game")


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move(1)

Tank.seize_developed = True
print("[notice] seize mode develope is compleated")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()


for unit in attack_units:
    unit.attack(1)

for unit in attack_units:
    unit.damaged(randint(5, 21))

game_oveer()
