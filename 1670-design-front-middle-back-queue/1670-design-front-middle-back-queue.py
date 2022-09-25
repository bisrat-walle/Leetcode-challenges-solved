class FrontMiddleBackQueue:

    def __init__(self):
        self.first = []
        self.second= []
    
    def size(self):
        return len(self.first)+len(self.second)
    
    def empty(self):
        return self.size() ==0
    
    def pushFront(self, val: int) -> None:
        self.first.insert(0, val)
        size = self.size()
        if len(self.first) > len(self.second)+1:
            self.second.insert(0, self.first.pop())

    def pushMiddle(self, val: int) -> None:
        size = self.size()
        if len(self.first) == len(self.second)+1:
            self.second.insert(0, self.first.pop())
            self.first.append(val)
        else:
            self.first.append(val)

    def pushBack(self, val: int) -> None:
        self.second.append(val)
        if len(self.first) < len(self.second):
            self.first.append(self.second.pop(0))

    def popFront(self) -> int:
        if self.empty():
            return -1
        res = self.first.pop(0)
        size = self.size()
        if len(self.first) < len(self.second):
            self.first.append(self.second.pop(0))
        return res
        

    def popMiddle(self) -> int:
        if self.empty():
            return -1
        print(self.first, self.second)
        res = self.first.pop()
        if len(self.first) < len(self.second):
            self.first.append(self.second.pop(0))
        return res

    def popBack(self) -> int:
        if self.empty():
            return -1
        if not self.second:
            res = self.first.pop()
        else:
            res = self.second.pop()
        size = self.size()
        if size >= 2 and len(self.first) > len(self.second)+1:
            self.second.insert(0, self.first.pop())
        return res


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()