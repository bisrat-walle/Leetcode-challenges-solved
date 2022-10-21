class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.indexes = defaultdict(set)

    def insert(self, val: int) -> bool:
        res = not self.indexes[val]
        self.arr.append(val)
        self.indexes[val].add(len(self.arr)-1)
        # print(f"After inserting {val} {self.arr} {self.indexes}")
        return res
        

    def remove(self, val: int) -> bool:
        if not self.indexes[val]:
            return False
        index = self.indexes[val].pop()
        # print(self.arr, self.indexes)
        tobeswapped = self.arr[-1]
        self.arr[index] = tobeswapped
        self.indexes[val].discard(index)
        self.indexes[tobeswapped].add(index)
        self.indexes[tobeswapped].discard(len(self.arr)-1)
        self.arr.pop()
        # print(f"After deleting {val} {self.arr} {self.indexes}")
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()