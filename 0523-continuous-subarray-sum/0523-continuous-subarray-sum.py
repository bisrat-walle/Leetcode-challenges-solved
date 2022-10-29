class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        runningSum = 0
        mapping = {0: 0}
        n = len(nums)
        for index in range(n):
            num = nums[index]
            runningSum += num
            if runningSum%k in mapping:
                if index != mapping[runningSum%k]:
                    return True
            else:
                mapping[runningSum%k] = index+1
        return False