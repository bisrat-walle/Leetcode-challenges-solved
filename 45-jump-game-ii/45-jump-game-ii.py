class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dp(index):
            if index >= len(nums)-1:
                return 0
            if index in memo:
                return memo[index]
            memo[index] = float("inf")
            for i in range(1, nums[index]+1):
                if index+i not in memo:
                    memo[index+i] = dp(index+i)
                memo[index] = min(memo[index], 1+memo[index+i])
            return memo[index]
        return dp(0)