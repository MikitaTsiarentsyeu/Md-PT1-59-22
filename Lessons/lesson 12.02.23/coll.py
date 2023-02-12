import random

class Collection:

    def __init__(self, *items) -> None:
        self.__items = []
        if items:
            self.__items.extend(items)

    # def get_items(self): #VERY BAD APPROACH
    #     return self.__items

    def add(self, item):
        if item not in self.__items:
            self.__items.append(item)

    def remove(self, item):
        if item in self.__items:
            self.__items.remove(item)

    def __len__(self):
        return len(self.__items)

    def __iter__(self):
        self._iterable_items = list(self.__items)
        random.shuffle(self._iterable_items)
        self._iterable_index = 0
        return self

    def __next__(self):
        if self._iterable_index >= len(self._iterable_items):
            del self._iterable_items
            del self._iterable_index
            raise StopIteration
        else:
            item = self._iterable_items[self._iterable_index]
            self._iterable_index += 1
            return item

    def __add__(self, other):
        if isinstance(other, Collection):
            return Collection(*(self.__items+list(other)))

    def __str__(self) -> str:
        return f"{Collection.__name__}({', '.join([str(x) for x in self.__items])})"

    def __getitem__(self, key):
        try:
            return self.__items[key]
        except IndexError:
            raise IndexError("Collection index out of range")

    def __setitem__(self, key, value):
        try:
            if value not in self.__items:
                self.__items[key]=value
        except IndexError:
            self.add(value)

c = Collection(1,2,3,4,5)
print(list(c))
print(len(c))

c1 = Collection(1,2,3)
c2 = Collection(4,5,6)
print(list(c1+c2))

c[100] = 100
print(c)

c = Collection(1,2,3)


