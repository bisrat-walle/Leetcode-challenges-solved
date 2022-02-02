class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = 1
        zero = 0
        for i in range(0, n):
            if nums[i] == 0:
                zero += 1
            else:
                p *= nums[i]
        an = [0]*n
        if zero == 0:
            for i in range(n):
                an[i] = int(p/nums[i])
        if zero == 1:
            for i in range(n):
                if nums[i] == 0:
                    an[i] = p
        return an