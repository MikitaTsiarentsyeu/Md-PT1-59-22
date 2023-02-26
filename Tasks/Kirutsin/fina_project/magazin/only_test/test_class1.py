class Mag:
    __colors = ['black', 'red', 'white']

    def __init__(self, brand, color, size):
        self.__brand = brand
        self.set_color(color, True)
        self.__size = size

    def get_brand(self):
        return self.__brand.upper()

    def get_color(self):
        return self.__color

    def get_size(self):
        return self.__size

    def set_brand(self, brand):
        self.__brand = brand

    def set_color(self, color, init=False):
        if color in Mag.__colors:
            self.__color = color
        elif init:
            self.__color = Mag.__colors[0]

    def set_size(self, size):
        self.__size = size

    color = property(get_color, set_color)

    def mag_crash(self):
        print("Crash!!!!!!!!")


x = Mag(brand="abibas", color="green", size="big")
x.color("red")
print(x.color)