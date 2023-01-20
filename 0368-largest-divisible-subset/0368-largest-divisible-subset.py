class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        mapping = {}
        dp = [1 for i in range(n)]
        max_length = 1
        index = 0
        for i in range(n):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    mapping[i] = j
            
            if max_length < dp[i]:
                max_length = dp[i]
                index = i
        
        current = index
        ans = []
        while True:
            ans.append(nums[current])
            if current not in mapping:
                break
            current = mapping[current]
        ans.reverse()
        return ans