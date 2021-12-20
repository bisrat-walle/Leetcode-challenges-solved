class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n = len(nums)
        nums = [int(i) for i in nums]
        nums.sort()
        if k > n:
            return nums[0]
        return str(nums[n-k])
        