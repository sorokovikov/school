from typing import Any


class PowerSet:

    def __init__(self):

        self.storage = []

    def size(self) -> int:

        return len(self.storage)

    def put(self, value: Any) -> None:

        if not self.get(value):
            self.storage.append(value)

    def get(self, value: Any) -> bool:

        return value in self.storage

    def remove(self, value: Any) -> bool:

        if self.get(value):
            self.storage.remove(value)
            return True
        return False

    def intersection(self, set2: "PowerSet") -> "PowerSet":

        if self.size() <= set2.size():
            return self.__intersection(self, set2)
        return self.__intersection(set2, self)

    def __intersection(self, set1: "PowerSet", set2: "PowerSet") -> "PowerSet":

        set3 = PowerSet()
        for value in set1.storage:
            if set2.get(value):
                set3.put(value)
        return set3

    def union(self, set2: "PowerSet") -> "PowerSet":

        set3 = self.copy()
        for value in set2.storage:
            set3.put(value)
        return set3

    def difference(self, set2: "PowerSet") -> "PowerSet":

        set3 = PowerSet()
        for value in self.storage:
            if not set2.get(value):
                set3.put(value)
        return set3

    def issubset(self, set2: "PowerSet") -> bool:

        if set2.size() > self.size():
            return False

        for value in set2.storage:
            if not self.get(value):
                return False
        return True

    def copy(self) -> "PowerSet":

        new_power_set = PowerSet()
        for value in self.storage:
            new_power_set.put(value)
        return new_power_set
