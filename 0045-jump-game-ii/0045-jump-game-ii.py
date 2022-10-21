class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dp(index):
            if index >= len(nums)-1:
                return 0
            an = float("inf")
            for i in range(1, nums[index]+1):
                if index + i not in memo:
                    memo[index+i] = 1+dp(index+i)
                an = min(an,memo[index+i])
            return an
        return dp(0)