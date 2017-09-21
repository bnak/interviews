# Implement a set-like data structure that supports Insert, Remove, and GetRandomElement efficiently.
# Example: If you insert the elements 1, 3, 6, 8 and remove 6, the structure should contain [1, 3, 8].
# Now, GetRandom should return one of 1, 3 or 8 with equal probability.

import random


class DataStructure():
    def __init__(self):
        self.store = {}

    def insert(self, item):
        self.store[item] = self.store.get(item, 1)

    def remove(self, item):
        self.store.pop(item)

    def get_random_element(self):
        keys = self.store.keys()
        return keys[random.randint(0, len(keys) - 1)]


def main():
    data_structure = DataStructure()
    data_structure.insert(1)
    data_structure.insert(3)
    data_structure.insert(6)
    data_structure.insert(8)

    print data_structure.store.keys()
    print data_structure.get_random_element()

    data_structure.remove(6)

    print data_structure.store.keys()
    print data_structure.get_random_element()


if __name__ == "__main__":
    main()
