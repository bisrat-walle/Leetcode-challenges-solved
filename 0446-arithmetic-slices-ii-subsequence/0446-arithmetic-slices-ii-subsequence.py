class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
            [1, 3, 5, 7, 9]
            
            
            
            
        """
        
        n = len(nums)
        dp = [defaultdict(int) for i in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                d = nums[i]-nums[j]
                ans += dp[j][d]
                dp[i][d] += 1 + dp[j][d]
        return ans
        
        
        
        