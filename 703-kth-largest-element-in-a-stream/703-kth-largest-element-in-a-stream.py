import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(nums)
        self.k = k
        

    def add(self, val: int) -> int:
        # heapq.heappush(self.nums, val)
        # heapCopy = [i for i in self.nums]
        
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # print(self.nums)
        if self.k > len(self.nums) or self.k <= 0:
            return
        return self.nums[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)