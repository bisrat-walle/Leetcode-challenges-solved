class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.recencyList = []
        

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.recencyList.remove(key)
            self.recencyList.append(key)
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache.keys():
            del self.cache[self.recencyList.pop(0)]
            
        if key in self.cache.keys():
            self.recencyList.remove(key)
        
        self.cache[key] = value
        self.recencyList.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)