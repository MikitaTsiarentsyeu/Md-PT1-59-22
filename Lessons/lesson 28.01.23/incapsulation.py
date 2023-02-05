

class Duster:

    __colors = ['black', 'red', 'white']

    def __init__(self, make, model, power, charge, color):
        self.__make = make
        self.__model = model
        self.__power = power
        self.__charge = charge
        self.set_color(color, True)

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model.upper()

    def test(self):
        return self.__color

    def set_color(self, color, init=False):
        if color in Duster.__colors:
            self.__color = color
        elif init:
            self.__color = Duster.__colors[0]

    color = property(test, set_color)

    def get_warranty_info(self):
        print("I'm in a good state, don't give me to any master!")

d = Duster("Samsung", "76g987liu", "70", "600", "green")
# d.make = "Samsung"
# d.model = "jhgfu67to8w3f7i"

print(d.get_model())
# d.set_color("blue")
# print(d.get_color())

d.color = "red"
print(d.color)