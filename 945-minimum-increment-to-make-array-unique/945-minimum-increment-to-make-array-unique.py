class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(len(nums)+nums[-1])
        dup = 0
        an = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dup += 1
                an -= nums[i]
            else:
                free = min(dup, nums[i] - nums[i-1] - 1)
                an += free * (free+1) //2 + free * nums[i-1]
                dup -= free
        return an