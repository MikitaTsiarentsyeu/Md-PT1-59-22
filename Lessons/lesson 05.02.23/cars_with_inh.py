class Engine:

    def __init__(self, power, volume):
        self.__power = power
        self.__volume = volume

    def get_power(self):
        return self.__power

    def get_volume(self):
        return self.__volume

    power = property(get_power)
    volume = property(get_volume)

class Vehicle:

    def move(self):
        print("Look mum, I'm moving!")

class Car(Vehicle):

    def __init__(self, make, model):
        self.__make = make
        self.__model = model

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    make = property(get_make)
    model = property(get_model)

    def move(self):
        super().move()
        print("Wroom-wroom!")

    def beep(self):
        print("BEEP!")

class SerialCar(Car):

    def __init__(self, make, model, engine):
        super().__init__(make, model)
        self.engine = engine

    def get_engine(self):
        return self.__engine

    def set_engine(self, engine):
        self.__engine = engine

    engine = property(get_engine, set_engine)


class SuperCar(Car):

    def __init__(self, make, model, power, volume):
        super().__init__(make, model)
        self.__engine = Engine(power, volume)

    def get_power(self):
        return self.__engine.power

    power = property(get_power)

vw = SerialCar('vw', 'golf', Engine(160, 2.0))

ff = SuperCar('ferrari', 'la ferrari', 300, 6.0)