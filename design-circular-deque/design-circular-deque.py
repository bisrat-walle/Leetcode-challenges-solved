class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.queue == []:
            return False
        self.queue.pop(0)
        return True

    def deleteLast(self) -> bool:
        if self.queue == []:
            return False
        self.queue.pop()
        return True

    def getFront(self) -> int:
        if self.queue == []:
            return -1 
        else:
            return self.queue[0]

    def getRear(self) -> int:
        if self.queue == []:
            return -1
        else:
            return self.queue[-1]

    def isEmpty(self) -> bool:
        return self.queue == []

    def isFull(self) -> bool:
        return len(self.queue) == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()