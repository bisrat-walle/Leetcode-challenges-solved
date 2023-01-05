class Allocator:

    def __init__(self, n: int):
        self.size = n
        self.allocated = set()
        self.store = defaultdict(set)

    def allocate(self, size: int, mId: int) -> int:
        cur = 0
        n = self.size
        found = False
        while cur < n and not found:
            
            if cur not in self.allocated:
                cnt = 1
                temp = cur
                while temp+1 < n and temp+1 not in self.allocated:
                    temp += 1
                    cnt += 1
                if cnt >= size:
                    found = True
                    break
                else:
                    cur = temp
            cur += 1
        
        if not found:
            return -1
        
        for i in range(size):
            self.allocated.add(cur+i)
            self.store[mId].add(cur+i)
        
        return cur
            

    def free(self, mId: int) -> int:
        for i in self.store[mId]:
            self.allocated.discard(i)
        ans = len(self.store[mId])
        self.store[mId] = set()
        return ans


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)