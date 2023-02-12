class Animal:

    def SaySomething(self):
        print("Hello!")
    
    def __str__(self) -> str:
        return "Hello!"

class Dog(Animal):

    def SaySomething(self):
        print("Woof")

    def __str__(self) -> str:
        return "Woof"

class Cat(Animal):

    def SaySomething(self):
        print("Meow")
    
    def __str__(self) -> str:
        return "Meow"

class Human(Animal): pass

    


animals = [Dog(), Cat(), Human(), Animal(), 34, "test"]

for a in animals:
    print(a)