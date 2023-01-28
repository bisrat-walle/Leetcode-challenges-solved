class SummaryRanges:

    def __init__(self):
        self.arr = []

    def addNum(self, value: int) -> None:
        self.arr.append(value)
        self.arr.sort()
        
    def getIntervals(self) -> List[List[int]]:
        ans = []
        index = 0
        while index < len(self.arr):
            first = self.arr[index]
            while index+1 < len(self.arr) and ( self.arr[index+1] == self.arr[index] + 1 or \
                                               self.arr[index] == self.arr[index+1]):
                index += 1
            
            ans.append([first, self.arr[index]])
            index += 1
        
        return ans
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()