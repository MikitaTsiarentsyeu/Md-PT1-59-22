class Dog:

    name = ""
    breed = ""
    color = ""

    def get_info(self):
        print(f"Hello, I'm {self.name} the {Dog.__name__}, {self.color} {self.breed}")

d = Dog()
d.name = "Zephyrka"
d.breed = "wss"
d.color = "white"

d.get_info()
print(Dog.breed, Dog.color, Dog.name)
print(type(d))

Dog.tail_length = 30
print(d.tail_length)

d1 = Dog()

d.second_name = "polar fire"
print(d.second_name)

d1.second_name