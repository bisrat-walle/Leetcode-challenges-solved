from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return ""
        max_index = self.mapping[key].bisect_right(timestamp)
        if max_index == 0: return ""
        return self.mapping[key].peekitem(max_index-1)[1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)