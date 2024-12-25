import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, cords=[0, 0, 0]):
        self._cords = cords
        self.speed = speed

    def move(self, dx, dy, dz):
        new_x = dx * self.speed + self._cords[0]
        new_y = dy * self.speed + self._cords[1]
        new_z = dz * self.speed + self._cords[2]
        if new_x > 0 and new_y > 0 and new_z > 0:
            self._cords[0] = new_x
            self._cords[1] = new_y
            self._cords[2] = new_z
        else:
            print("It's too deep, i can't dive :(")

    def get_cords(self):
        print(f'X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        list_eggs = [1, 2, 3, 4]
        eggs = random.choice(list_eggs)
        print(f'Here are(is) {eggs} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = self._cords[2] - (abs(dz) * self.speed // 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird, Animal):
    sound = "Click-click-click"


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()