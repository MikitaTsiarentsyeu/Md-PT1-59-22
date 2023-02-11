class Food:

    def __init__(self, name, cat):
        self.name = name
        self.cat = cat

class Animal:

    _cats = []

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"eating {food.name}")

    def phe(self):
        print('phe...')

    def try_food(self, food):
        if food.cat in self._cats:
            return True

        return False

class DependencyEater(Animal):

    def eat(self, food):
        if food.cat in self._cats:
            Animal.eat(self, food)
        else:
            super().phe()

class Carnivore(DependencyEater):

    _cats = ["meat"]

class Herbivore(DependencyEater):

    _cats = ["plant"]


class Omnivore(Herbivore, Carnivore):

    _cats = ["meat", "plant"]

    def eat(self, food):
        if Herbivore.try_food(self, food):
            Herbivore.eat(self, food)
        elif Carnivore.try_food(self, food):
            Carnivore.eat(self, food)
        else:
            super().phe()


meat = Food("Stake", "meat")
grass = Food("Grass", "plant")

tigger = Carnivore("Tigger")
rabbit = Herbivore("Rabbit")

piglet = Omnivore("Piglet")
piglet.eat(meat)
piglet.eat(grass)

print(Omnivore.mro())