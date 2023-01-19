class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        (total - (subarraySum)) % p = 0
        total%p = subarraySum%p
        
        (prefix[j] - prefix[i]) % p = rem
        prefix[j]%p - prefix[i]%p = rem
        prefix[j]%p - rem
        
        """
        
        total = sum(nums)
        rem = total % p
        if rem == 0:
            return 0
        
        n = len(nums)
        ans = n
        mapping = {0: 0} # {prefix%p: index}
        runningSum = 0
        for j in range(n):
            num = nums[j]
            runningSum = (runningSum + num) % p
            i_rem = (runningSum - rem) % p
            if i_rem in mapping:
                ans = min(ans, j - mapping[i_rem] + 1)
            mapping[runningSum] = j+1
            
        return ans if ans < n else -1