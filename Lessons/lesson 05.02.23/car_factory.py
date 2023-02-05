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


class SerialCar:

    def __init__(self, make, model, engine):
        self.__make = make
        self.__model = model
        self.engine = engine

    def set_engine(self, engine):
        self.__engine = engine

    def get_engine(self):
        return self.__engine

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    make = property(get_make)
    model = property(get_model)
    engine = property(get_engine)

e1 = Engine(160, 2.0)
golf = SerialCar("vw", "golf", e1)

golf.engine = Engine(180, 2.0)
print(golf.engine.power)


class SuperCar:

    def __init__(self, make, model, power, volume):
        self.__make = make
        self.__model = model
        self.__engine = Engine(power, volume)

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_power(self):
        return self.__engine.power

    make = property(get_make)
    model = property(get_model)

ff = SuperCar("Ferrari", "la ferrari", 300, 6.0)