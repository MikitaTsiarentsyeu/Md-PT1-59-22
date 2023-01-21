
class Dog:

    name = ""
    color = ""
    breed = ""

    def introduce(self):
        print(f"hello, my name is {self.name}")

    def bork(self):
        print("B0000RK!!!111111")

print(type(Dog))
# print(Dog.name)
# Dog.bork()

d = Dog()
d.name = "Zephyrka"
d.color = "white"
d.breed = "wss"
d.bork()
d.introduce()

d2 = Dog()
d2.name = "Funtic"
d2.color = "white"
d2.breed = "samoyed"
d2.introduce()

