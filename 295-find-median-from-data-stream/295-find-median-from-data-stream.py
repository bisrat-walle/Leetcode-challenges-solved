from heapq import *

class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = [] 

    def addNum(self, num: int) -> None:
        min_heap_size = len(self.minheap)
        max_heap_size = len(self.maxheap)
        
        if min_heap_size == 0:
            heappush(self.minheap, num)
            return
        if max_heap_size == 0:
            if num > self.minheap[0]:
                cur = heappop(self.minheap)
                heappush(self.minheap, num)
                heappush(self.maxheap, -1*cur)
            else:
                heappush(self.maxheap, -1*num)
            return
        if num > self.minheap[0]:
            heappush(self.minheap, num)
        else:
            heappush(self.maxheap, -1*num)
        self.balance_heapsizes()
        

    def findMedian(self) -> float:
        # print(self.minheap, self.maxheap)
        if (len(self.minheap) + len(self.maxheap)) % 2 == 0:
            # print("Even", self.minheap[0], -1*self.maxheap[0])
            return (self.minheap[0] + -1*self.maxheap[0])/2
        # print("Odd", self.minheap[0])
        if self.minheap:
            return self.minheap[0]
    
    def balance_heapsizes(self):
        min_heap_size = len(self.minheap)
        max_heap_size = len(self.maxheap)
        if min_heap_size == max_heap_size or max_heap_size + 1 == min_heap_size:
            return
        if max_heap_size > min_heap_size:
            heappush(self.minheap, -1*heappop(self.maxheap))
            return
        heappush(self.maxheap, -1*heappop(self.minheap))
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()