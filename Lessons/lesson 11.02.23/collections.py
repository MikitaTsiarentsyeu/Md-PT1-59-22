class Collection:

    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def get_items(self):
        return self._items

    items = property(get_items)

class UniqueCollection(Collection):

    def add(self, item):
        if item not in self._items:
            super().add(item)

    
class SortedCollection(Collection):

    def add(self, item):
        super().add(item)
        self._items.sort()

class UniqueSortedCollection(SortedCollection, UniqueCollection):

    def add(self, item):
        return super().add(item)



c = UniqueSortedCollection()
c.add(3)
c.add(1)
c.add(1)
c.add(2)

print(c.items)