class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(index):
            left, right = index, len(nums)-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        
        index = len(nums) - 2
        while index > -1 and not nums[index+1] > nums[index]:
            index -= 1
        
        if index != -1:
            index2 = len(nums) - 1
            while nums[index2] <= nums[index]:
                index2 -= 1
            nums[index2], nums[index] = nums[index], nums[index2]
        
        reverse(index+1)
        