class Animal:

    def __init__(self, name) -> None:
        self.name = name

class FlyingAnimal(Animal):

    def __init__(self, name) -> None:
        super().__init__(name)

    def fly(self):
        print("I'm flying!")

class RunningAnimal(Animal):

    def __init__(self, name) -> None:
        super().__init__(name)

    def run(self):
        print("I'm running")

class SwimmingAnimal(Animal):

    def __init__(self, name) -> None:
        super().__init__(name)

    def swim(self):
        print("I'm swimming")


class Crow(FlyingAnimal, RunningAnimal): pass

class Capybara(RunningAnimal, SwimmingAnimal): pass

class Duck(SwimmingAnimal, RunningAnimal, FlyingAnimal):

    def __init__(self, name) -> None:
        super().__init__(name)

c = Duck("ducky")
c.swim()
c.fly()
c.run()

print(Duck.__mro__)