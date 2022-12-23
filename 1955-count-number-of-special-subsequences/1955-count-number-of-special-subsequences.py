class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        dp = [0 for i in range(3)]
        for num in nums:
            if num == 0:
                dp[0] = 2 * dp[0] + 1
            elif num == 1:
                dp[1] = (2*dp[1] + dp[0]) % mod
            else:
                dp[2] = (dp[1] + 2*dp[2]) % mod

        return dp[-1]%mod