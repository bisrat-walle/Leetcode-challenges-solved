class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        for i in nums:
            if i != 0:
                temp.append(i)
        for i in range(len(temp)):
            nums[i] = temp[i]
        for i in range(len(temp), len(nums)):
            nums[i] = 0
        