class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        for index in range(len(nums)):
            j = index-1
            while j > -1 and nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                j -= 1
            
        if nums[0] == "0":
            return "0"

        return "".join(nums)