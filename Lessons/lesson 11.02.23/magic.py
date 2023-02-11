class FreightTrain:

    def __init__(self, cart_count):
        self.cart_count = cart_count

    def __str__(self):
        return f"I'm a train of {self.cart_count} carts, choo-choo!"

    def __int__(self):
        return self.cart_count

    def __add__(self, other):
        if isinstance(other, int):
            return FreightTrain(self.cart_count+other)
        try:
            return FreightTrain(self.cart_count+other.cart_count)
        except:
            raise TypeError(f"Cannot add {type(other)} to FreightTrain")
    
    def __eq__(self, other):
        if not isinstance(other, FreightTrain):
            return False

        return self.cart_count == other.cart_count

        
        

train = FreightTrain(10)
print(int(train))

t = FreightTrain(10)
print(FreightTrain(10)+10)

print(t+t == FreightTrain(10)+10)

str(FreightTrain(10)+10)

print(str(int.__add__(2, 3)))


print(str(FreightTrain.__add__(FreightTrain(10), FreightTrain(10))))

FreightTrain(10)-FreightTrain(10)
