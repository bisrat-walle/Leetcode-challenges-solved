class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def gcd(a, b):
            if not b:
                return a
            return gcd(b, a%b)
        ans = 0
        for index in range(len(nums)):
            cur = nums[index]
            for j in range(index, len(nums)):
                cur = gcd(cur, nums[j])
                if cur == k:
                    ans += 1
        return ans