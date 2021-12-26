class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        n = len(nums)
        for i in range(1, n):
            j = i-1
            num = nums[i]
            while j >= 0:
                if nums[j]+num < num+nums[j]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                else:
                    break
                j -= 1
        if nums[0] == "0":
            return "0"
        return "".join(nums)