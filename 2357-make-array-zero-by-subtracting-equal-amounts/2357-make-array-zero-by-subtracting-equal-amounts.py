class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        current = 0
        for num in nums:
            if num > current:
                ans += 1
                current = num
        return ans