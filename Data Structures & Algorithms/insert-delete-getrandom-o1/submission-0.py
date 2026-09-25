from collections import defaultdict
class RandomizedSet:

    def __init__(self):
        self.hashSet = defaultdict(int)
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.hashSet:
            return False
        self.hashSet[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashSet:
            return False
        index = self.hashSet[val]
        lastVal = self.array[-1]
        self.array[index], self.array[-1] = self.array[-1], self.array[index]
        self.hashSet[lastVal] = index
        del self.hashSet[val]
        self.array.pop()
        return True

    def getRandom(self) -> int:
        if self.array:
            return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()