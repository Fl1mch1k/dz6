
import random

class Dog:
    def __init__(self, name='Dog', home=None):
        self.name = name
        self.home = home
        self.satiety = 50
        self.joy = 50
    def get_home(self):
        self.home = House()

    def eat(self):
        if self.home.food <= 0:
            self.find("food")
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def find(self, manage):
        if manage == "food":
            print("Found food")
            self.home.food += 50
            self.joy += 10


    def chill(self):
        self.satiety -= 10
        self.joy += 10

    def sleep(self):
        self.satiety -= 50
        self.joy += 10


    def days_indexes(self, day):
        day = f"Today the {day} of {self.name}'s life"
        print(f"{day:=^50}", '\n')
        Dog_indexess = self.name + "'s indexes"
        print(f"{Dog_indexess:=^50}", '\n')
        print(f'Satiety - {self.satiety}')
        print(f'joy - {self.joy}')
        home_indexess = "Home indexxes"
        print(f"{home_indexess:^50}", '\n')
        print(f'Food - {self.home.food}')


    def is_alive(self):
        if self.joy < 0:
            print("Depression.....")
            return False
        if self.satiety < 0:
            print("Dead....")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print('Found a new booth')
            self.get_home()

        dice = random.randint(1, 3)
        if self.satiety < 10:
            print("I'll go eat")
            self.eat()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Time to sleep")
            self.sleep()
        elif dice == 3:
            print("Find")
            self.find()



class House:
    def __init__(self):
        self.food = 0

nick = Dog(name="Geralt")

for day in range(1, 8):
    if nick.live(day) == False:
        break
