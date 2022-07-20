class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [nums[0]]
        for index in range(1, len(nums)):
            self.prefix.append(self.prefix[index-1]+nums[index])

    def sumRange(self, left: int, right: int) -> int:
        if not left:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)