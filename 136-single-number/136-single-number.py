class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        an = nums[0]
        return ([an] + [an := an ^ num for num in nums[1:]])[-1]
        # an = nums[0]
        # for num in nums[1:]: an ^= num
        # return an