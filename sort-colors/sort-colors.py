class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0, 0, 0]
        for i in nums:
            temp[i] += 1
        i, j, k = temp
        for m in range(i):
            nums[m] = 0
        for m in range(i, j+i):
            nums[m] = 1
        for m in range(j+i, j+i+k):
            nums[m] = 2
        