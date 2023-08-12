import random


# Without list - slow
class RandomizedSet:

    def __init__(self):
        self.randomMap = {}

    def insert(self, val: int) -> bool:
        if val in self.randomMap:
            return False

        self.randomMap[val] = len(self.randomMap)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomMap:
            return False

        del self.randomMap[val]

        return True

    def getRandom(self) -> int:
        return random.choice(list(self.randomMap.keys()))


# With list - faster O(1)
class RandomizedSet2:

    def __init__(self):
        self.randomMap = {}
        self.randomList = []

    def insert(self, val: int) -> bool:
        if val in self.randomMap:
            return False

        self.randomMap[val] = len(self.randomMap)
        self.randomList.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomMap:
            return False

        # Update the value (index) of key (val) in dictionary
        # Move current last element to the index of val in list and pop the last element (val already replaced, no need to swap)
        index = self.randomMap[val]
        value = self.randomList[-1]
        self.randomMap[value] = index
        self.randomList[index] = value

        self.randomList.pop()
        del self.randomMap[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.randomList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()