class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.arr:
            if start <= i < end:
                return False
            if start <= j < end:
                return False
            if i <= start <= j:
                return False
            if i <= end-1 <= j:
                return False
        self.arr.append([start, end-1])
        return True
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)