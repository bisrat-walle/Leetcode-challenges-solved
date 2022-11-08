class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        tot = 0
        for num in nums:
            tot ^= num
        for i in range(32):
            if tot & (1<<i):
                break
        
        a = b = 0
        for num in nums:
            if num & (1<<i):
                a ^= num
            else:
                b ^= num
        return [a, b]